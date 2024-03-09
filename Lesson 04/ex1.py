kwh = float(input("Nhap so kwh: "))
if kwh <= 50:
    tong = kwh * 1700
elif 50 < kwh <= 100:
    tong = 50 * 1700 + (kwh - 50)*1900
elif 100 < kwh <= 200:
    tong = 50 * 1700 + 50 * 1900 + (kwh -100) * 2100
else:
    tong = 50 * 1700 + 50 * 1900 + 100 * 2100 + (kwh -200) * 3000
print(tong)