x = int(input("Nhap x: "))
n =int(input("Nhap n: "))
s=0
for i in range(1,n+1):
    tu=tu*x
    mau=1
    for j in range(1,i+1):
        mau=mau*j
    s=s+tu/mau
print("s{0},{1}={2}".format(x,n,s))

