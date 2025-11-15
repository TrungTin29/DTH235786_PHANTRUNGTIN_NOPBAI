from math import sqrt
def so_le(so):
    return so % 2 != 0
def so_chan(so):
    return so % 2 == 0
def dem_so_le(lst):
    dem = 0
    for i in lst:
        if so_le(i):
            dem += 1
    return dem

def dem_so_chan(lst):
    dem = 0
    for i in lst:
        if not so_le(i):
            dem += 1
    return dem

def kiem_Tra_So_Nguyen_To(so):
    if so <2:
        return False
    for i in range(2, int(sqrt(so))+1):
        if so % i == 0:
            return False
    return True

print("Nhập số phần tử: ")
n = int(input())
lst = []
for i in range(n):
    num = int(input(f"Nhập phần tử thứ {i+1}: "))
    lst.append(num)
print("Có", dem_so_le(lst), "số lẻ")
print("Có", dem_so_chan(lst), "số chẵn")

for i in lst:
    print(f"{i}: ", end="")
    print("Lẻ" if so_le(i) else "Chẵn", end=", ")
    print("Nguyên tố" if kiem_Tra_So_Nguyen_To(i) else "Không phải nguyên tố")