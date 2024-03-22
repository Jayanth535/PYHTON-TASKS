def check_occurnaces(li):
    set1=set(li)
    list2=[]
    for i in set1:
        res=i,li.count(i)
        list2.append(res)
    return list2
n=int(input("Enter how many elements in the list contain: "))
print("Enter",n,"elements:")
li=[]
for i in range(n):
    num=int(input())
    li.append(num)
print(check_occurnaces(li))