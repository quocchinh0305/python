import math
#Hoạt động 3
print("Kết quả hoạt động 3")
so_nguyen=15
so_thuc=4.2
so_phuc=3+4j
print(type(so_nguyen),type(so_thuc),type(so_phuc))
print(float(so_nguyen))
print(int(so_thuc))
a=-7
b=2.6789
c,d=17,5
print(abs(a))     #giá trị tuyệt đối
print(round(b))   #làm tròn
print(round(b,2)) #làm tròn 2 chữ số thap phân
print(pow(c,2))   #mu 2
print(divmod(c,d)) #trả về thương dư
a,b,c=1,-3,2
detal=pow(b,2)-4*a*c
x1=(-b+math.sqrt(detal))/(2*a)
x2=(-b-math.sqrt(detal))/(2*a)
print(f"Detal={detal}")
print(f"Nghiệm x1={round(x1,2)},x2={round(x2,2)}")
#Hoạt động 4
print("Kết quả hoạt động 4")
cau="Lập trình python rất thú vị"
print(cau[0])
print(cau[-1])
print(cau[4:10])
print(cau[:8])
print(cau[11:])
print(cau[::-1])
print(cau==cau[::-1])
ten="Nam"
ten_moi="T"+ten[1:]
print(ten_moi)
cau=" Tôi đang HOC Python rất vui   "
print(cau.strip())  #bỏ khoảng trắng 2 đầu
print(cau.strip().upper())    #in hoa
print(cau.strip().lower())     # in thường
print(cau.strip().replace("HOC","hoc"))
print(cau.strip().split())      #tách thành các từ
print(len(cau.strip().split()))  #đếm số tu trong câu
print(cau.count("o"))           #đếm số lần ký tự xuất hiện
print(cau.find("Python"))       #vị trí bắt đầu của Python
print(cau.strip().startswith("Tôi")) #ktra xem có bắt đầu bằng từ tôi kh
print(cau.strip().endswith("vui"))   #ktra xem có kết thúc bằng từ tôi kh
print("-".join(["Python","that","thu","vị"]))
ho_ten_tho="       vương       quốc        chính      "
ho_ten=" ".join(ho_ten_tho.split()).title()
print(ho_ten)