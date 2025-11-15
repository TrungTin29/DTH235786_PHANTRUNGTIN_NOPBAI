import re
''' 
thư viện re là gì

Thư viện re là thư viện tích hợp sẵn trong Python dùng để xử lý chuỗi bằng biểu thức chính quy (regular expressions).
Nó cho phép tìm kiếm, kiểm tra, thay thế, tách chuỗi theo các mẫu phức tạp.
Một số hàm phổ biến của re là: re.search(), re.match(), re.findall(), re.sub().'''
def NegativeNumberInString(s):
     # Tìm tất cả số nguyên âm có dạng -số, không phải --số
    numbers = re.findall(r'(?<!-)-\d+', s)
    for num in numbers:
        print(num)

chuoi = "abc-5xyz-12k9l--p"
NegativeNumberInString(chuoi)