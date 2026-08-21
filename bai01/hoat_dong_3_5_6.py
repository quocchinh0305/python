print("Kết quả hoạt động 3")
ten="Nguyen Van A"
diem_toan=8.5
diem_van=7.0
so_luong_mon_hoc=2
MUC_LUONG_TOI_THIEU=5000000
print("Họ và tên:",ten)
print("Điểm toán:",diem_toan)
print("Điểm văn:",diem_van)
print("Số lượng môn học:",so_luong_mon_hoc)
print("Mức lương tối thiếu:",MUC_LUONG_TOI_THIEU)
print("Kết quả hoạt động 5")
a=17
b=5
print("a+b=",a+b)
print("a-b=",a-b)
print("a*b=",a*b)
print("a/b=",a/b)
print("a//b=",a//b)
print("a%b=",a%b)
print("a**b=",a**b)
diem=6.5
tuoi=20
la_loai_kha=(diem>=6.5) and (diem<8.0)
print("Điểm đạt loai khá: ",la_loai_kha)
tuoi_tac= (tuoi<18) or(tuoi>60)
print("Tuổi dưới 18  hoặc trên 60: ",tuoi_tac)
phu_dinh_tuoi=not tuoi_tac
print("Phủ định điều kiện tuổi: ",phu_dinh_tuoi)
x=10
x+=5
print("x sau +=5",x)
x-=3
print("x sau -=3",x)
x*=2
print("x sau *=2",x)
x/=3
print("x sau /=3",x)
x//=5
print("x sau //=5",x)
x**=2
print("x sau **=5",x)
danh_sach=[1,2,3,"python"]
print("3 có trong danh_sach không?",3 in danh_sach)
danh_sach_copy=danh_sach
print("danh_sach và danh_sach_copy có cùng trỏ vào 1 list không?",danh_sach_copy is danh_sach)
print("Kết quả biểu thức 1:",2+3*4**2)
print("Kết quả biểu thức 2:",(2+3)*4**2)
print("Kết quả biểu thức 3:",10>5 and 3<1 or not False)
print("Kết quả hoạt động 6")
bien=10
print(bien,type(bien))
bien="Xin chào"
print(bien,type(bien))
bien=3.14
print(bien,type(bien))
ho_ten="Nguyen Van A"
diem_toan=8.5
diem_ly=7.5
diem_hoa=9.0
dtb=(diem_toan+diem_ly+diem_hoa)/3
la_gioi=dtb>=8.0
la_kha=dtb >=6.5 and dtb<8.0
la_trung_binh=dtb>=5.0 and dtb<6.5
la_yeu =dtb<5.0
print(ho_ten, "- DTB:", round(dtb, 2))
print("Dat loai Gioi?", la_gioi)
print("Dat loai Kha?", la_kha)

print("Dat loai Trung binh?", la_trung_binh)
print("Dat loai Yeu?", la_yeu)
print("Kieu du lieu cua la_gioi:", type(la_gioi))