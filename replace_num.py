def replace_num():
    for i in range(len(list1)):
        if list1[i] == ele:
            list1[i] = rp_num
    return list1

n=int(input("Enter the number of elements should be in the list: "))
print("Enter the",n,"elements:\n")
list1=[]
for i in range(n):
    num=int(input())
    list1.append(num)
ele=int(input("Select an elementin the above list to replace: "))
rp_num=int(input("Enter the number that the selected element is replaced with: "))
if ele in list1:
    res=replace_num()
    print(res)
else:
    print("Sorry!, I can't replace",'\"',ele,'\"',"with ",'\"',rp_num,'\"')
    print("Because",'\"',ele,'\"',"is  not found in the list")