def nhap_matrix(m,n, name):
    print(f"Nhập ma trận {name}: ")
    matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            val = int(input(f"Nhập phần tử [{i}][{j}]: "))
            row.append(val)
        matrix.append(row)
    return matrix

def cong_matrix(A,B):
    m,n = len(A), len(A[0])
    C = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(A[i][j] + B[i][j])
        C.append(row)
    return C

def hoan_vi_matrix(M):
    m,n = len(M), len(M[0])
    T = []
    for j in range(n):
        row = []
        for i in range(m):
            row.append(M[i][j])
        T.append(row)
    return T

def xuat_matrix(M, name):
    print(f"Ma trận {name}:")
    for row in M:
        for val in row:
            print(val, end='\t')
        print()

#Nhập kích thước ma trận
print("Nhập số dòng: ")
m = int(input())
print("Nhập số cột: ")
n = int(input())

A = nhap_matrix(m,n,"A")
B = nhap_matrix(m,n,"B")

C = cong_matrix(A,B)
xuat_matrix(A,"A")
xuat_matrix(B,"B")
xuat_matrix(C,"C = A + B")

A_T = hoan_vi_matrix(A)
B_T = hoan_vi_matrix(B)
xuat_matrix(A_T,"A^T")
xuat_matrix(B_T,"B^T")
    