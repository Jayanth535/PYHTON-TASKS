def multiplicate(n) :
  limit=int(input("enter the limit you want to caluculate : "))
  for i in range(1,limit+1) :
    print(n,"*",i,"=",n*i)
n=int(input("Enter a table number to caluculate : "))
multiplicate(n)

# Output:
# Enter a table number to caluculate : 2
# enter the limit you want to caluculate : 10
# 2 * 1 = 2
# 2 * 2 = 4
# 2 * 3 = 6
# 2 * 4 = 8
# 2 * 5 = 10
# 2 * 6 = 12
# 2 * 7 = 14
# 2 * 8 = 16
# 2 * 9 = 18
# 2 * 10 = 20