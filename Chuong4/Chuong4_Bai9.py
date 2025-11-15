from math import sqrt
n = int(input("Nhập n: "))
S = 0
for i in range(n, 0, -1):
    S = sqrt(i + S)

print("Giá trị căn bậc 2 lồng nhau là:", S)