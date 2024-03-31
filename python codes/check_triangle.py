def triangle_check(angl1,angl2,angl3) :
        if angl1 + angl2 + angl3 == 180 :
            return "It is a valid triangle."
        else :
            return "The angles are not valid and hence It is not a valid triangle."
def check_sides(a,b,c):
    if a + b <=c and b + c <=a and c + a <=b :
        print("The sides are not valid ")
a=int(input("Enter 1st side: "))
b=int(input("Enter 2nd side: "))
c=int(input("Enter 3rd side: "))
print(check_sides(a,b,c))
print("The Sides are Valid.")
angl1=int(input("Enter first angle: "))
angl2=int(input("Enter second angle: "))
angl3=int(input("Enter third angle: "))
print(triangle_check(angl1,angl2,angl3))
