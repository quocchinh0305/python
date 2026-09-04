import math
print("Kết quả hoạt động 4")
toa_do=(3,5)
print(toa_do,type(toa_do))
x,y=toa_do
print("x=",x,"-y=",y)
a,b=10,20
a,b=b,a
print("a=",a,"b=",b)
c,d=17,5
thuong_du=divmod(c,d)
thuong,du=thuong_du
print(f"{c} chia {d} được thương {thuong},dư {du}")
print("Kết quả hoạt động 5")
diem_a=(2,3)
diem_b=(7,8)
xa,ya=diem_a
xb,yb=diem_b
khoang_cach=math.sqrt((xa-xb)**2+(ya-yb)**2)
print(f"Khoảng cách giữa{diem_a} và {diem_b}là: {round(khoang_cach,2)}")
cac_diem=[(0,0),(3,4),(6,8)]
khoang_cach=[ math.hypot(*diem) for diem in cac_diem]
print(f"Khoảng cách các điểm đến (0,0) là { khoang_cach}")
