
while True:
    n = int(input("Nhap vao so nguyen duong: "))
    dem=0
    for i in range(1,n+1):
        if n % i ==0:
            dem+=1
    if dem==2:
        print(n,"La so nguyen to")
    else:
        print(n,"Khong la so nguyen to")
    hoi=input("Tiep khong? (c/k): ")
    if hoi is "k":
        break
print("BYE!")
