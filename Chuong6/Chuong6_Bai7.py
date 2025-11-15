# Viết chương trình nhập vào một dãy các số theo thứ tự tăng, nếu nhập sai
# quy cách thì yêu cầu nhập lại. In dãy số sau khi đã nhập xong

print("Nhập số phần tử: ")
n = int(input())
lst = []

print("Mời bạn nhập các phần tử theo thứ tự tăng dần: ")
for i in range(n):
    while True:
        num = int(input(f"Nhập số thứ {i+1}: "))
        if i == 0 or num > lst[-1]:
            lst.append(num)
            break
        else:
            print("Số không hợp lệ, vui lòng nhập lại. ")
print("Dãy số đã nhập là: ")
print(lst)