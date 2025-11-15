
a = int(input("Nhap vao thang trong nam (1-12): "))
while a < 1 or a > 12:
    a = int(input("Nhap sai! Vui long nhap lai thang trong nam (1-12): "))

if a in [1,2,3]:
    print("Quy 1")
elif a in [4,5,6]:
    print("Quy 2")
elif a in [7,8,9]:
    print("Quy 3")
else:
    print("Quy 4")