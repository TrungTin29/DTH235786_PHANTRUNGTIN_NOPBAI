# Kiem tra nam nhuan

year = int(input("Nhap vao mot nam: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "la nam nhuan.")
else:
    print(year, "khong phai la nam nhuan.")