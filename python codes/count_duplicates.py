def count_duplicates():
    count=0
    for ele in list1:
        if ele in list1:
            count+=1
        return (ele,count)
n=int(input())
list1=[]
for i in range(n):
    num=int(input())
    list1.append(num)
print(count_duplicates())