str=input("Enter the string to check: ")
res=str[::-1]
if str==res:
    print(str,"is a Palindrome number")
else:
    print(str,"is not a Palindrome number")
    

""" OUTPUT:
TEST-1: 
     Enter the string to check: 123321
    123321 is a Palindrome number
TEST-2:
     Enter the string to check: 989
     989 is a Palindrome number
TEST-3:
     Enter the string to check: yateesh
     yateesh is not a Palindrome number
TEST-4:
     Enter the string to check: madam
     madam is a Palindrome number """