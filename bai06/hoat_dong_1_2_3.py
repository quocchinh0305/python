print("Kết quả hoạt động 1")
def uscln(a,b):
    while b!=0:
        a,b=b,a%b
    return a
def bscnn(a,b):
        return (a*b)/uscln(a,b)
def kiem_tra_nguyen_to(n):
    if n<2:
     return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def kiem_tra_so_hoan_thien(n):
    tong_uoc=0
    for i in range(1,n):
        if n%i==0:
            tong_uoc+=i
    return tong_uoc==n
print(uscln(12,6))
print(bscnn(4,6))
print(kiem_tra_nguyen_to(12))
print(kiem_tra_so_hoan_thien(6))
def in_loi_chao(ten):
    print(f"Xin chào,{ten}!")
    return
def chia_lay_thuong_du(a,b):
    return a//b,a%b
in_loi_chao("Việt Anh")
thuong,du=chia_lay_thuong_du(12,5)
print(f"Thương: {thuong},dư:{du}")
print("Kết quả hoạt động 2:")
def gioi_thieu(ten,tuoi=10,lop="Chưa có"):
    print(f"Ten:{ten}-tuoi:{tuoi}-lop:{lop}")
gioi_thieu("An")
gioi_thieu("Bình",20)
gioi_thieu("Chi",lop="CNTT01")
gioi_thieu("Chi",lop="CNTT02",tuoi=19)
print("Kết quả hoạt động 3")
def tinh_tong(*arg):
    tong=0
    for so in arg:
        tong+=so
    return tong
print(tinh_tong(1,2,3))
print(tinh_tong(5,10,15,20,25))
print(tinh_tong())
def in_thong_tin(ho_ten,tuoi,**kwargs):
   print(f"Ten:{ho_ten}-tuoi:{tuoi}")
   for khoa,giatri in kwargs.items():
       print(f"{khoa}:{giatri}")
in_thong_tin("Nguyễn Văn A",20,lop="CNTT01",que_quan="Hà Nội")
in_thong_tin("Trần Thị An",21,email="an0305@gmail.com")

