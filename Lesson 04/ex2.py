a = int(input("Nhap so trang can in: "))
b = int(input("Nhap loai giay can in: "))

if b == 1:
    soto = a
else:
    if a % 2 == 0:
        so_to = a/2
    else:
        soto = int(a/2 +1)
        
print(f"so to giay can la: {soto}")
        