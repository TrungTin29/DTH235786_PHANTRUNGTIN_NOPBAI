from math import log
def nhapA():
    while True:
        try:
            print("Nhập vào số dương a: ")
            a = int(input())
            if a > 1:
                return a
            else:
                print("a phải lớn hơn 1, mời nhập lại!")
        except ValueError:
            print("Vui lòng nhập số hợp lệ!")

def nhapX():   
    while True:
        try:
            print("Nhập vào số dương x: ")
            x = float(input())
            if x > 0:
                return x
            else:
                print("x phải là số dương, mời nhập lại!")
        except ValueError:
            print("Vui lòng nhập số hợp lệ!")


a = nhapA() 
x = nhapX()
logax = (log(x)/log(a))

print("Logarit cơ số", a, "của", x, "là:", logax)
