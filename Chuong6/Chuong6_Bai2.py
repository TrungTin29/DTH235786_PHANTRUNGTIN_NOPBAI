from random import randrange


lst = []

print("Nhập số phần tử: ")
n = int(input())
for i in range(n):
    lst.append(randrange(0, 100))
print("List sau khi tạo ngẫu nhiên: ")
print(lst)
x = int(input("Nhập số cần thêm vào list: "))
lst.append(x)
print("List sau khi chèn: ")
print(lst)
k = int(input("Mời nhập số để xoá: "))
while lst.count(k) > 0:
    lst.remove(k)
    print("list sau khi xoá: ")
    print(lst)

def CheckDoiXung(lst):
    for i in range(len(lst)):
        for i in range(len(lst)):
            if lst[i] != lst [len(lst)-i-1]:
                return False
    return True
kt = CheckDoiXung(lst)
if kt == True:
    print("list đối xứng")
else:
    print("list không đối xứng")