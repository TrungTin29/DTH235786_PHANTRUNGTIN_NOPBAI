from math import sqrt
print("Nhập toạ độ điểm A(xA, yA)")
xA = float(input("xA = "))
yA = float(input("yA = "))
print("Nhập toạ độ điểm B(xB, yB)")
xB = float(input("xB = "))
yB = float(input("yB = "))

do_dai = sqrt((xB - xA) ** 2 + (yB - yA) ** 2)
print("Độ dài đoạn thẳng AB là:", do_dai)