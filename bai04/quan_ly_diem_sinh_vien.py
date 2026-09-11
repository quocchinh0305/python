quan_ly_diem={
    "Nguyễn Việt Anh":[8.0,7.5,9.0],
    "Phạm Tuấn Dương":[6.0,6.5,5.5],
    "Vương Quốc Chính":[9.0,9.5,8.5],
}
quan_ly_diem["Phạm Thị Dương"]=[7.0,8.0,7.5]
quan_ly_diem["Phạm Tuấn Dương"][0]=7.0
diem_trung_binh={}
for ho_ten,danh_sach_diem in quan_ly_diem.items():
    diem_trung_binh[ho_ten]=round(sum(danh_sach_diem)/len(danh_sach_diem),2)
print("Bảng điểm trung bình: ")
for ho_ten,dtb in diem_trung_binh.items():
    dat_loai_gioi=dtb>=8.0
    print(f"{ho_ten:<15}-DTB:{dtb:<5}-Đạt loại giỏi?{dat_loai_gioi}")