def replace_num(ele, rep_num):
    for i in range(len(list1)):
        if list1[i] == ele:
            list1[i] = rep_num
    return list1
n=int(input("Enter the number of elements should be in the list: "))
print("Enter the",n,"elements:")
list1=[]
for i in range(n):
    num=int(input())
    list1.append(num)
ele=int(input("Select an element in the above list to replace: "))
rep_num=int(input("Enter the number that the selected element is replaced with: "))
if ele in list1:
    print("The original list is: ",list1)
    print("After replacing",'\"',ele,'\"',"with",'\"',rep_num,'\"',"the new list is ==>",replace_num(ele, rep_num))
else:print("Sorry!, you can't replace",'\"',ele,'\"',"with ",'\"',rep_num,'\"',"\nbecause",'\"',ele,'\"',"is not found in the list")