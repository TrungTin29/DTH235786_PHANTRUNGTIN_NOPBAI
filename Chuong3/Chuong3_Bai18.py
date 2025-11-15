n = int(input("Nhap chieu cao n: "))

# Hinh 1
def hinh1(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j ==0 or j == n-1:
                print("*",end=" ")
            else:
                print(" ", end=" ")
        print()
def hinh2(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1  or i+j == n-1:
                print("*",end=" ")
            else:
                print(" ", end=" ")         
    print()

def hinh3(n):
    for i in range(1, n+1):
        print("* " * i)
def hinh4(n):
    for i in range(n):
        for j in range(n):
            if j == 0 or i == n-1:
                print("*",end=" ")
            else:
                print(" ", end=" ")
        print()

print("Hinh 1:")
hinh1(n)
print("\nHinh 2:")
hinh2(n)
print("\nHinh 3:")
hinh3(n)
print("\nHinh 4:")
hinh4(n)   