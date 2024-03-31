def calculate_hypotenuse(a,b) :
     hypotenuse=((a**2+b**2)**0.5)
     return hypotenuse
sum=0
angles_list=[]
for i in range(1,4):
    print("Enter the angle ",i,":")
    angles=int(input())
    angles_list.append(angles)
    sum+=angles
for i in range(len(angles_list)):
    if angles_list[i]==90 and sum==180:
        print("It is a valid right angled triangle")
        a=int(input("Enter the first side :"))
        b=int(input("Enter the second side :"))
        print("The hypotenuse side is:",calculate_hypotenuse(a,b))
    else:
        print("It is not a valid right angled traingle")
        break