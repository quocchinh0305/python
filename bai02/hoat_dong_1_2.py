#Hoạt động 1
print("Kết quả hoạt động 1")
ho_ten=input("Nhập họ tên: ")
nam_sinh=int(input("Nhập năm sinh: "))
diem_tb=float(input("Nhập điểm trung bình: "))
print("Python","là","ngôn","ngữ","lập trình",sep="-")
print("Dòng 1",end=" | ")
print("Dòng 2")
print(f"Họ tên: {ho_ten}-Năm sinh: {nam_sinh}-DTB: {diem_tb:.2f}")
print("Ho ten: {}-Nam sinh: {}-DTB: {}".format(ho_ten, nam_sinh, diem_tb))
print("Ho ten:%s-Năm sinh:%d-DTB:%.2f"%(ho_ten, nam_sinh, diem_tb))
#Hoạt động 2
print("Kết quả hoạt động 2")
"""
Chu thich/dostring nhieu dong: 
Chương trình quản lý sinh viên buổi 2
"""
ho_ten="Vương Quốc Chính" #biến lưu họ tên
s1="Xin chào"
s2="Bạn có khỏe không"
s3='''Đây là
một chuỗi
nhiều dòng'''
s4="Đường dẫn C:\\Python\\data"
s5=r"Đường dẫn raw:C:\Python\data"
s6="Tôi tên là\"Nam\",còn bạn tên gì"
print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print(s6)