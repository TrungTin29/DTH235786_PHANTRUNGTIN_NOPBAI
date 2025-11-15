# PT bac 2 ax^2 + bx + c = 0
import math
a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
c = float(input("Nhap c: "))

if(a == 0):
    #bx+c=0
    if(b ==0 and c==0):
        print("PT vo so nghiem")
    elif b==0 and c!=0:
        print("PT vo nghiem")
    else:
        print("PT co nghiem x=  ",-c/b)
else:
    deta = b**2 - 4*c*a
    if deta <0:
        print("PT vo nghiem")
    elif deta == 0:
        print("PT co nghiem kep x1=x2= ",-b/(2*a))
    else:
        print("PT co 2 nghiem phan biet")
        print("x1= ",(-b + math.sqrt(deta))/(2*a)) 
        print("x2= ",(-b - math.sqrt(deta))/(2*a))
