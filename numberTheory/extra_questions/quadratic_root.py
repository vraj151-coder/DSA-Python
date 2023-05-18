import math

def quadratic_root(a,b,c):
    discriminant=b*b-(4*a*c)
    if discriminant<0:
        print("No root of this equation")
    val=math.sqrt(discriminant)/(2*a)
    root1=-b/(2*a)+val
    root2=-b/(2*a)-val
    if root1==root2:
        print(f"The root of this equation is : {int(root1)}")
    else:
        print(f"The roots of this equation are : {int(root1)} and {int(root2)}")

quadratic_root(1,-7,12)
    