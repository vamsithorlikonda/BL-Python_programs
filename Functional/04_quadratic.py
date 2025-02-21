import math
def quadratic(a,b,c):
    delta=(b*b) - (4*a*c)
    if delta <0:
        return print(f"not real roots")
    Root_1 = (-b + math.sqrt(delta))/(2*a)
    Root_2 = (-b - math.sqrt(delta))/(2*a)
    return print(f"root1{Root_1} and root2{Root_2} for {a}x^2+{b}*x+{c}")
a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
quadratic(a,b,c)