from fontTools.misc.cython import returns

danh_sach_sv=[
    {"ma_sv":"101","ten":"Nguyễn Thị Việt Anh","lop":"DH14C1","toan":6,"ly":7,"hoa":5,"dtb":8,"xep_loai":""},
{"ma_sv":"102","ten":"Phạm Thị Dương","lop":"DH14C1","toan":10,"ly":8,"hoa":6,"dtb":8,"xep_loai":""},
]
def tim_kiem_sv_theo_ma(ma_sv):
    for sv in danh_sach_sv:
        if sv["ma_sv"].lower()==ma_sv.lower():
            return sv
    return None
def nhap_diem(loi_nhac):
    while True:
        try:
            diem=float(input(loi_nhac))
            if 0<=diem<=10:
                return diem
            print("Điểm phải nằm từ khoảng 0 đến 10.")
        except ValueError:
            print("Dữ liệu vui lòng nhập số thực.")
def tim_kiem_sv():
 tu_khoa=input("Nhập thông tin sinh viên cần tìm")
 ket_qua=[
    sv for sv in danh_sach_sv
    if tu_khoa in sv["ma_sv"].lower() or tu_khoa in sv["ten"].lower() or tu_khoa in sv["xep_loai"].lower()
  ]
 if not  ket_qua:
    print("Không tìm thấy sinh viên")
    return
 print("\nKết quả tìm kiếm: ")
 for sv in ket_qua:
     print(
         f"-MSV: {sv['ma_sv']}|Họ tên:{sv['ten']}|Lớp:{sv['lop']}|Điểm toán:{sv['toan']}|Điểm lý:{sv['ly']}|Điểm hóa:{sv['hoa']}|Điểm tb:{sv['dtb']}|Xếp loại:{sv['xep_loai']}")
def hien_thi_danh_sach():
    if not danh_sach_sv:
        print("Danh sách sinh viên trống")
        return
    print("\n"+"="*80)
    for sv in danh_sach_sv:
        dtb=sv["dtb"]
        if dtb>=8.0:
            sv["xep_loai"]="Gioi"
        elif dtb>=6.5:
            sv["xep_loai"]="Kha"
        elif dtb>=5.0:
            sv["xep_loai"]="Trung bình"
        else:
            sv["xep_loai"]="Yếu"
        print(
            f"-MSV: {sv['ma_sv']}|Họ tên:{sv['ten']}|Lớp:{sv['lop']}|Điểm toán:{sv['toan']}|Điểm lý:{sv['ly']}|Điểm hóa:{sv['hoa']}|Điểm tb:{sv['dtb']}|Xếp loại:{sv['xep_loai']}")
def them_sinh_vien():
        t=input("Nhập mã sinh viên mới:").strip().upper()
        if tim_kiem_sv_theo_ma(t) is not None:
            print(f"Mã sinh viên {t}  đã tồn tại.")
            return
        ten=input("Nhập họ và tên sinh viên:").strip().title()
        lop=input("Nhập lớp:").strip().upper()
        toan=nhap_diem("Nhập điểm toán: ")
        ly=nhap_diem("Nhập điểm lý: ")
        hoa=nhap_diem("Nhập điểm hóa:")
        diem_tb=round((toan+ly+hoa)/3,2)
        danh_sach_sv.append({
            "ma_sv":t,
            "ten":ten,
            "lop":lop,
            "toan":toan,
            "ly":ly,
            "hoa":hoa,
            "dtb":diem_tb,
         })
        print(f"Đã thêm sinh viên {ten} thành công")

def sua_dau_diem():
    ma_sv=input("Nhập mã sinh viên cần sửa điểm").strip().upper()
    sv=tim_kiem_sv_theo_ma(ma_sv)
    if sv is None:
        print(f"Không tìm thấy sinh viên ")
        return
    print(f"Đang sửa điểm cho sv {sv['ten']}(Điểm cũ-Toán:{sv['toan']}|Lý:{sv['ly']}|Hóa:{sv['hoa']}")
    sv['toan']=nhap_diem("Sửa điểm toán")
    sv['ly']=nhap_diem("Sửa điểm lý")
    sv['hoa']=nhap_diem("Nhập điểm hóa")
    sv['dtb']=round((sv['toan']+sv["ly"]+sv["hoa"])/3,2)
    print(f"Cập nhật đầu điểm cho sv {sv['ten']} thành công")
def xoa_sinh_vien():
    ma_sv = input("Nhập mã sinh viên cần xóa:").strip().upper()
    sv = tim_kiem_sv_theo_ma(ma_sv)
    if sv is not None:
       danh_sach_sv.remove(sv)
       print(f"Đã xóa sv {sv['ten']} thành công")
    else:
        print(f"Không tìm thấy sv ")
def hienthimenu():
    print("QUẢN LÝ SINH VIÊN")
    print("1.Hiển thị danh sách sinh viên ")
    print("2.Thêm sinh viên mới")
    print("3.Tìm kiếm sinh viên")
    print("4.Xóa sinh viên")
    print("5.Sửa  thông tin sinh viên")
    print("6.Thoát chương trình")
if __name__ == "__main__":
    while True:
        hienthimenu()
        lua_chon=input("Nhập lựa chọn:").strip()
        if lua_chon=="1":
            hien_thi_danh_sach()
        elif lua_chon=="2":
            them_sinh_vien()
        elif lua_chon=="3":
            tim_kiem_sv()
        elif lua_chon=="4":
            xoa_sinh_vien()
        elif lua_chon=="5":
            sua_dau_diem()
        elif lua_chon=="6":
            print("Thoát chương trình")
            break;
        else:
            print("Lựa chọn kh hợp lệ vui lòng chọn từ 1-6")


