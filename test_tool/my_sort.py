def mysort(inList,dir):
    newList=[]
    while len(inList)>0:
        if dir:
            minData = max(inList)
        else:
            minData =min(inList)
        newList.append(minData)
        inList.remove(minData)
    return newList

alist=[0,8,5,1,2]
print(mysort(alist))
print(mysort(alist),True)


