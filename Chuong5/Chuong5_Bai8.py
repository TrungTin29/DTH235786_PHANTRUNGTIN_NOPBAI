import os

def lay_ten_file(path):
    return os.path.basename(path) # Lấy ra tên file với phần mở rộng
def lay_ten_file_khong_mo_rong(path):
    return os.path.splitext(os.path.basename(path))[0] 
# Lấy ra tên file không có phần mở rộng

duong_dan = r'd:music\canhphiyen.mp3'
print("Tên file: ", lay_ten_file(duong_dan))
print("Tên file không có phần mở rộng: ", lay_ten_file_khong_mo_rong(duong_dan))