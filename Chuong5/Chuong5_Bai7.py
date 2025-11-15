def toi_uu_chuoi_danh_tu(s):
   # Loại bỏ khoảng trắng dư thừa và tách các từ
   tu = s.strip().split()
   # Viết hoa ký tự đầu tiên của mỗi từ, các ký tự còn lại viết thường
   tu_hoa = [word.capitalize() for word in tu]
   ket_qua = ' '.join(tu_hoa)
   return ket_qua


chuoi = input("Nhập chuỗi danh từ: ")
print("Chuỗi danh từ tối ưu: ", toi_uu_chuoi_danh_tu(chuoi))