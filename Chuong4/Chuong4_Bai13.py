def tong_uoc_so(n):
    tong = 0
    for i in range(1,n,):
        if n % i == 0:
            tong+=i
    return tong

def so_hoan_thien(n):
    return tong_uoc_so(n) == n

def so_thinh_vuong(n):
    return tong_uoc_so(n) > n   

n = int(input("Nhập số nguyên dương n: "))
if so_hoan_thien(n):
    print(n, "là số hoàn thiện.")
elif so_thinh_vuong(n):
    print(n, "là số thịnh vượng.")
else:
    print(n, "không phải là số hoàn thiện hoặc số thịnh vượng.")