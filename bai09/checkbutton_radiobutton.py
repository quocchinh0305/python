import tkinter as tk
cua_so=tk.Tk()
cua_so.title("Ví dụ Checkbutton")
cua_so.geometry("300x220")
tk.Label(cua_so,text="Chọn sở thích của bạn",font=("Arial",12)).pack(pady=10)
bien_doc_sach=tk.BooleanVar()
bien_the_thao=tk.BooleanVar()
bien_am_nhac=tk.BooleanVar()
tk.Checkbutton(cua_so,text="Đọc sách",variable=bien_doc_sach).pack(anchor="w",padx=30)
tk.Checkbutton(cua_so,text="Thể Thao",variable=bien_the_thao).pack(anchor="w",padx=30)
tk.Checkbutton(cua_so,text="Âm nhạc",variable=bien_am_nhac).pack(anchor="w",padx=30)
def xem_lua_chon():
    print("Doc sach",bien_doc_sach.get())
    print("Thể thao",bien_the_thao.get())
    print("Âm nhạc",bien_am_nhac.get())
tk.Button(cua_so,text="Xem lựa chọn",command=xem_lua_chon).pack(pady=15)
cua_so.mainloop()

cua_so=tk.Tk()
cua_so.title("Vi du Radiobutton")
cua_so.geometry("300x200")
bien_loai_tai_khoan = tk.StringVar(value="ca_nhan") # gia tri mac dinh
tk.Label(cua_so, text="Chon loai tai khoan:", font=("Arial", 12)).pack(pady=10)
tk.Radiobutton(cua_so, text="Ca nhan", variable=bien_loai_tai_khoan,
value="ca_nhan").pack(anchor="w", padx=30)
tk.Radiobutton(cua_so, text="Doanh nghiep", variable=bien_loai_tai_khoan,
value="doanh_nghiep").pack(anchor="w", padx=30)
def xem_loai_tai_khoan():
  nhan_ket_qua.config(text=f"Ban da chon: {bien_loai_tai_khoan.get()}")
tk.Button(cua_so, text="Xac nhan", command=xem_loai_tai_khoan).pack(pady=10)
nhan_ket_qua = tk.Label(cua_so, text="")
nhan_ket_qua.pack()
cua_so.mainloop()