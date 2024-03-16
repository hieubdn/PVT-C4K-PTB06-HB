an = float(input("Nhập chiều cao của An: "))
minh = float(input("Nhập chiều cao của Minh: "))
lan = float(input("Nhập chiều cao của Lan: "))

if an >= minh and an >= lan:
    cao_nhat = an
    nguoi_cao_nhat = "An"
elif minh >=an and minh>=lan:
    cao_nhat = minh
    nguoi_cao_nhat = "Minh"
else:
    cao_nhat= lan
    nguoi_cao_nhat= "Lan"
print(nguoi_cao_nhat, "là người cao nhất.")