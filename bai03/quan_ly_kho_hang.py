kho_hang=[
    ("Bàn phím",25000,10),
    ("Chuột",15000,20),
    ("Màn hình",2500000,5)
]
kho_hang.append(("Tai nghe",300000,15))
kho_hang.remove(("Chuột",15000,20))
print("Danh sách kho hàng: ")
for ten,gia ,so_luong in kho_hang:
    print(f"{ten:<12}-Giá{gia:>10,}-số lượng: {so_luong}")
tong_gia_tri=0
for ten,gia ,so_luong in kho_hang:
    tong_gia_tri+=gia*so_luong
print(f"Tổng giá trị kho hàng: {tong_gia_tri} VND")
