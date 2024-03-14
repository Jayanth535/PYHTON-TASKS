str=input("Enter the string to check: ")
res=str[::-1]
print(res)
if str==res:
    print(str,"is a Palindrome number")
else:
    print(str,"is not a Palindrome number")