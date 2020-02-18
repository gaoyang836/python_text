def middle(*some):
    sorted(some)
    l=int(len(some)/2)
    if  (len(some))%2 == 0 :
        s=(some[l]+some[l-1])/2 
    elif (len(some))%2 == 1 :
        s=some[l]
    else :
        pass    
    return s

print(middle(-1,-5,3.5,8))


# foo = [1,3,5,7,9]
# print(list(map(lambda x:x*x,foo) ))