import math
x = float(input("Nhap vao x: "))
n = int(input("Nhap vao n: "))

def tinh_S(x, n):
    s = 0
    for i in range(n+1):
        mu = 2*i+1 
        s +=x**mu/math.factorial(mu)
    return s

ket_qua = tinh_S(x, n)
print(f"Gia tr cua S({x}, {n}) la: ", {ket_qua})
    
