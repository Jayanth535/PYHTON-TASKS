def check(list1):
    list2=[]
    for i in list1:
        if i not in list2:
            list2.append(i)
    return list2
list1=[5,4,3,2,1,5,4,5,]
print(check(list1))
