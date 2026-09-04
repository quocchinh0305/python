danh_sach_sv=[(8.5,"An"),(7.0,"Bình"),(9.2,"Chi"),(6.5,"Dung")]
danh_sach_sv.append((8.0,"Em"))
danh_sach_sv.remove((7.0,"Bình"))
danh_sach_sv[0]=(9.0,danh_sach_sv[0][1])
print(danh_sach_sv)
print("Chi có trong danh sách  kh?",(9.2,"Chi") in danh_sach_sv)
danh_sach_sv.sort()
print("Danh sách sau khi sắp xếp tăng dần :")
for diem,ten in danh_sach_sv:
    print(f"{ten}-{diem}")
print("Danh sách sau khi sắp xếp giảm dần: ")
for diem,ten in danh_sach_sv:
    print(f"{ten}-{diem}")