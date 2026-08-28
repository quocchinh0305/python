ho_ten=input("Nhập họ tên: ")
sdt=input("Nhập số điện thoại: ")
email=input("Nhập email: ")
ho_ten_chuan=" ".join(ho_ten.split()).title()
sdt_hop_le=len(sdt)==10
email_hop_le="@" in email
print(f"Họ tên(đã chuẩn hóa:  {ho_ten_chuan}")
print(f"Số điện thoại hợp lệ ( đủ 10 ký tự)?{sdt_hop_le}")
print(f"Email hợp lệ( có ký tự @)?{email_hop_le}")
