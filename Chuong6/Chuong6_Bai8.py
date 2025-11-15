print("Nhập số phần tử: ")
n = int(input())
lst = []
for i in range(n):
    num = int(input(f"Nhập phần tử thứ {i+1}: "))
    lst.append(num)

lst.sort(reverse=True)

print("Dãy số sau khi sắp xếp giảm dần là: ")
print(lst)