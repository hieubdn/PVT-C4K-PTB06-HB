so_trang_can_in = int(input("Nhap so trang can in: "))
loai_giay = int(input("Nhap loai giay can in: "))
if loai_giay == 1:
    so_to = so_trang_can_in
else:
    if so_trang_can_in % 2 == 0:
        so_to = so_trang_can_in/2
    else:
        so_to = int(so_trang_can_in/2 +1)
print(f"so to giay can la: {so_to}")
