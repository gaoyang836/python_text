import contextlib
import pymysql.cursors
import requests
import secrets
import hashlib

# 生成随机数字符串

def makeNonceStr():
    return secrets.token_hex(16)

# 签名

def makeSign(data, signKey):
    # 字典排序
    dic = dict(sorted(data.items(), key=lambda d: d[0]))
    e = ''
    for k, v in dic.items():
        if v != '':
            d = '{k}={v}'.format(k=k, v=v)
            e += d+'&'
    e += 'key={}'.format(signKey)
    return makeMd5(e)

# 把返回值xml转字典


def xml2dict(pre_xml):
    soup = BeautifulSoup(pre_xml, features='xml')
    xml = soup.find('xml')
    if not xml:
        return 'error'
    return dict([(item.name, item.text) for item in xml.find_all()])

# 字典转xml


def dictxml(data):
    s = '<xml>'
    for k, v in data.items():
        c = '<{k}>{v}</{k}>'.format(k=k, v=v)
        s += c
    s += '</xml>'
    return s

# 构造Md5

def makeMd5(str):
    m = hashlib.md5()
    m.update(str.encode("utf8"))
    sign = m.hexdigest()
    return sign.upper()

url = "https://api.mch.weixin.qq.com/pay/orderquery"

def makeR(sub_mch_id, out_trade_no):
    dt = {
        'appid': 'xxxxxxxxxxx',
        'mch_id': 'xxxxxxxxxxx',
        'sub_mch_id': sub_mch_id,
        'transaction_id': '',
        'out_trade_no': out_trade_no
    }
    dt['nonce_str'] = makeNonceStr()
    dt['sign'] = makeSign(dt, 'xxxxxxxxxxxxxxxx')
    dataXml = dictxml(dt)
    r = requests.post(url, data=dataXml)
    r.encoding = 'utf-8'

    res = xml2dict(r.text)
    return res


# 访问数据库
# 连接数据库
@contextlib.contextmanager
def mysql():
    conn = pymysql.connect(
        host='xxxxxxxxxxxx',
        port=3306,
        user='xxxxxx',
        passwd='xxxxxxxxx',
        db='xxxxxxx',
        charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    try:
        yield cursor
    finally:
        conn.commit()
        cursor.close()
        conn.close()


with mysql() as cursor:
    sql = "select out_trade_no,order_status from tp_order where uuid='xxxxxxxxxxxxxxx'"
    cursor.execute(sql)
    result = cursor.fetchall()
    status = {
      '1':'SUCCESS',
      '2':['REFUND','REVOKED','PAYERROR'],
      '0':['NOTPAY','USERPAYING'],
      '5':'CLOSED'
        }
    for data in result:
        res = makeR('1493057602',data['out_trade_no'])
        # 判断脚本返回值与库中状态
        if res.get('out_trade_no') is None:
            pass
        elif res.get('trade_state')=='SUCCESS'and res.get('out_trade_no')==status['1']:
            print('yes')
        elif res.get('trade_state')=='REFUND'and res.get('out_trade_no')==status['2']:
            print('yes')
        elif res.get('trade_state')=='NOTPAY'and res.get('out_trade_no')==status['0']:
            print('yes')
        elif res.get('trade_state')=='CLOSED'and res.get('out_trade_no')==status['5']:
            print('yes')
        else :
            print(res.get('out_trade_no'),res.get('trade_state'),'no') 

        # print(res.get('out_trade_no'),res.get('trade_state'))


  







