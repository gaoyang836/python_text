# -*-coding:utf-8 -*-

def get_type(obj):
    return type(obj)

def get_list():
    return [1,2,3,4]

def get_dict():
    return {"key":'abc',"key":123}


if __name__ == '__main__':
    print(get_type(123))
