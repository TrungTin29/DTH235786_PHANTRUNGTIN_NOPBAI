chuoi = input(("Nhập vào một chuỗi: "))

dem_in_hoa = 0
dem_in_thuong = 0
dem_chu_so = 0
dem_ky_tu_dạc_biet  =0 
dem_nguyen_am = 0
dem_phu_am = 0

nguyen_am = "aeiouAEIOUáàảãạâấầẩẫậăắằẳẵặéèẻẽẹêếềểễệíìỉĩịóòỏõọôốồổỗộơớờởỡợúùủũụưứừửữự"
for c in chuoi:
    if c.isupper():
        dem_in_hoa += 1
    if c.islower():
        dem_in_thuong +=1
    if c.isdigit():
        dem_chu_so +=1
    if not c.isalum() and not c.isspace():
        dem_ky_tu_dạc_biet +=1
    if c.lower() in nguyen_am:
        dem_nguyen_am +=1
    elif c.isalpha():
        dem_phu_am +=1
print("Số ký tự in hoa: ",dem_in_hoa)
print("Số ký tự in thường: ",dem_in_thuong)
print("Số ký tự chữ số: ",dem_chu_so)       
print("Số ký tự đặc biệt: ",dem_ky_tu_dạc_biet)
print("Số ký tự nguyên âm: ",dem_nguyen_am)
print("Số ký tự phụ âm: ",dem_phu_am)

