print("Kết quả hoạt động 1")
sinh_vien={
    "ho_ten":"Vương Quốc Chính",
    "nam_sinh":2004,
    "diem_tb":8.5,
}
print(sinh_vien["ho_ten"])
print(sinh_vien["diem_tb"])
print(sinh_vien.get("lop","Chua co"))
sinh_vien["lop"]="CNTT01"
sinh_vien["diem_tb"]=9.0
print(sinh_vien)
diem_cu=sinh_vien.pop("diem_tb")
print(sinh_vien,"-diem da xoa",diem_cu)
sinh_vien.update({"nam_sinh":2006,"email":"quocchinh0305@gmail.com"})
print(sinh_vien)
print("Kết quả hoạt động 2")
diem_mon_hoc={"Toán":8.0,"Lý":7.5,"Hóa":9.0,"Văn":6.5}
for mon in diem_mon_hoc.keys():
    print(mon)
for diem in diem_mon_hoc.values():
    print(f"{mon}:{diem}")
tong_diem=0
for diem in diem_mon_hoc.values():
    tong_diem+=diem
print("Điểm trung bình:",round(tong_diem/len(diem_mon_hoc),2))
print("Kết quả hoạt động 3")
diem_cong_diem={mon:round(diem+0.5,2) for mon,diem in diem_mon_hoc.items()}
print(diem_cong_diem)
ten_mon_viet_hoa={mon.upper() :diem for mon,diem in diem_mon_hoc.items()}
print(ten_mon_viet_hoa)
mon_hoc_ky1={ "Toán","Lý","Hóa","Văn"}
mon_hoc_ky2={ "Toán","Anh","Tin","Văn"}
print(mon_hoc_ky1&mon_hoc_ky2)
print(mon_hoc_ky1|mon_hoc_ky2)
print(mon_hoc_ky1 - mon_hoc_ky2)