from random import  randrange
print("Nhập số phần tử: ")
n = int(input())
lst =[]

while len(lst) < n:
    num = randrange(-100,100)
    if num not in lst:
        lst.append(num)

print("List ngẫu nhiên không trùng là: ")
print(lst)