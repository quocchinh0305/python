print("Kết quả hoạt động 4:")
so_luot_truy_cap=0
def tang_luot_truy_cap():
    global so_luot_truy_cap
    so_luot_truy_cap+=1
def vi_du_bien_local():
    so_luot_truy_cap=100
    print("Bên trong hàm,biến local=",so_luot_truy_cap)
tang_luot_truy_cap()
tang_luot_truy_cap()
print("Số lượt truy cập(global):",so_luot_truy_cap)
vi_du_bien_local()
print("Sau khi gọi hàm,biến global vẫn là: ",so_luot_truy_cap)
print("Kết quả hoạt động 5:")
danh_sach_so=[1,2,3,4,5]
binh_phuong=list(map(lambda x:x**2,danh_sach_so))
print(binh_phuong)
so_chan=list(filter(lambda x:x%2==0,danh_sach_so))
print(so_chan)
danh_sach_sv=[
    {"ten":"Việt Anh","diem":8.5},
    {"ten":"Việt Hoàng", "diem":10},
    {"ten":"Quốc Chính", "diem":9.5},
]
sap_xep_theo_diem=sorted(danh_sach_sv,key=lambda x:x["diem"])
sap_xep_giam_dan=sorted(danh_sach_sv,key=lambda x:x["diem"],reverse=True)
for sv in sap_xep_theo_diem:
    print(sv["ten"],"-",sv["diem"])
print("---------Giam dan-------")
for sv in sap_xep_giam_dan:
    print(sv["ten"],"-",sv["diem"])