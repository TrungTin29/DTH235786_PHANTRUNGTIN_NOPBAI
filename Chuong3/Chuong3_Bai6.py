def doc_so(n):
    don_vi = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    dac_biet = {1: "mốt", 4: "tư", 5: "lăm"}
    chuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]

    if n < 10:
        return don_vi[n] if n != 0 else "không"
    elif n < 20:
        if n == 10:
            return "mười"
        elif n == 15:
            return "mười lăm"
        else:
            return "mười " + don_vi[n % 10]
    else:
        hang_chuc = n // 10
        hang_dv = n % 10
        if hang_dv == 0:
            return chuc[hang_chuc]
        elif hang_dv in dac_biet and hang_chuc >= 2:
            return chuc[hang_chuc] + " " + dac_biet[hang_dv]
        else:
            return chuc[hang_chuc] + " " + don_vi[hang_dv]

n = int(input("Nhập số n (tối đa 2 chữ số): "))
if 0 <= n <= 99:
    print(doc_so(n))
else:
    print("Vui lòng nhập số từ 0 đến 99.")