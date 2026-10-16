import tkinter as tk
from tkinter import messagebox
cua_so=tk.Tk()
cua_so.title("Máy tính bỏ túi")
cua_so.geometry("320x420")
cua_so.resizable(False,False)
bieu_thuc=""
chuoi_nhap=tk.StringVar()
o_hien_thi=tk.Entry(cua_so,textvariable=chuoi_nhap,font=("Arial",18),width=35)
o_hien_thi.grid(row=0,column=0,padx=10,pady=10,columnspan=4)
def nhap_ky_tu(ky_tu):
    global bieu_thuc
    bieu_thuc+=str(ky_tu)
    chuoi_nhap.set(bieu_thuc)
def tinh_ket_qua():
    try:
        global bieu_thuc
        ket_qua=str(eval(bieu_thuc))
        chuoi_nhap.set(ket_qua)
        bieu_thuc=ket_qua
    except ZeroDivisionError:
        messagebox.showerror("Lỗi","Không thể chia cho số 0!")
        bieu_thuc=""
        chuoi_nhap.set("")
    except Exception:
        messagebox.showerror("Lỗi","Biểu thức không hợp lệ!")
        bieu_thuc=""
        chuoi_nhap.set("")
def xoa_man_hinh():
    global bieu_thuc
    bieu_thuc=""
    chuoi_nhap.set("")
danh_sach_nut=[
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
]
for (nhan,hang,cot) in danh_sach_nut:
    if nhan=="=":
        nut=tk.Button(cua_so,text=nhan,font=("Arial",14,"bold"),fg="white",bg="green",command=tinh_ket_qua)
    elif nhan=="C":
        nut=tk.Button(cua_so,text=nhan,font=("Arial",14,"bold"),bg="red",fg="white",command=xoa_man_hinh)
    else:
        nut=tk.Button(cua_so,text=nhan,font=("Arial",14,"bold"),command=lambda t=nhan: nhap_ky_tu(t))
    nut.grid(row=hang,column=cot,sticky="nsew",padx=3,pady=3)
for i in range(5):
    cua_so.grid_rowconfigure(i,weight=1)
for j in range(4):
    cua_so.grid_columnconfigure(j,weight=1)
cua_so.mainloop()