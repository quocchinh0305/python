import tkinter as tk
from tkinter import messagebox

from cau1 import them_san_pham, tim_kiem_theo_ten, tong_gia_tri_ton_kho


class QuanLySanPham(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quản lý sản phẩm (Tái sử dụng Câu 1)")
        self.geometry("650x600")
        self.resizable(False, False)

        self.danh_sach_sp = [
            {"MaSP": "SP001", "TenSP": "Bút bi Thiên Long", "Gia": 3000, "SoLuong": 150},
            {"MaSP": "SP002", "TenSP": "Vở học sinh 96 trang", "Gia": 8000, "SoLuong": 8},
            {"MaSP": "SP003", "TenSP": "Bút chì 2B", "Gia": 2500, "SoLuong": 200}
        ]

        khung_nhap = tk.LabelFrame(self, text="Thông tin sản phẩm", padx=10, pady=10)
        khung_nhap.pack(fill="x", padx=10, pady=10)

        tk.Label(khung_nhap, text="Mã SP:").grid(row=0, column=0, sticky="w", pady=5)
        self.entry_ma = tk.Entry(khung_nhap, width=30)
        self.entry_ma.grid(row=0, column=1, pady=5, padx=5)

        tk.Label(khung_nhap, text="Tên SP:").grid(row=1, column=0, sticky="w", pady=5)
        self.entry_ten = tk.Entry(khung_nhap, width=30)
        self.entry_ten.grid(row=1, column=1, pady=5, padx=5)

        tk.Label(khung_nhap, text="Giá:").grid(row=2, column=0, sticky="w", pady=5)
        self.entry_gia = tk.Entry(khung_nhap, width=30)
        self.entry_gia.grid(row=2, column=1, pady=5, padx=5)

        tk.Label(khung_nhap, text="Số lượng:").grid(row=3, column=0, sticky="w", pady=5)
        self.entry_soluong = tk.Entry(khung_nhap, width=30)
        self.entry_soluong.grid(row=3, column=1, pady=5, padx=5)

        btn_them = tk.Button(khung_nhap, text="Thêm sản phẩm", bg="#4CAF50", fg="white", font=("Arial", 10, "bold"),
                             command=self.xu_ly_them)
        btn_them.grid(row=4, column=0, columnspan=2, pady=10)

        timkiem = tk.LabelFrame(self, text="Tìm kiếm & Thống kê", padx=10, pady=10)
        timkiem.pack(fill="x", padx=10, pady=5)

        tk.Label(timkiem, text="Từ khóa tên:").grid(row=0, column=0, sticky="w")
        self.entry_search = tk.Entry(timkiem, width=20)
        self.entry_search.grid(row=0, column=1, padx=5)

        btn_search = tk.Button(timkiem, text="Tìm kiếm", command=self.xu_ly_tim_kiem)
        btn_search.grid(row=0, column=2, padx=5)

        btn_reset = tk.Button(timkiem, text="Hiển thị tất cả", command=self.hien_thi_tat_ca)
        btn_reset.grid(row=0, column=3, padx=5)

        btn_ton_kho = tk.Button(timkiem, text="Tổng tồn kho", bg="#FF9800", fg="white", command=self.xem_tong_ton_kho)
        btn_ton_kho.grid(row=0, column=4, padx=5)

        hienthi = tk.LabelFrame(self, text="Danh sách sản phẩm", padx=10, pady=10)
        hienthi.pack(fill="both", expand=True, padx=10, pady=10)

        self.listbox = tk.Listbox(hienthi, width=85, height=10)
        self.listbox.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(hienthi, orient="vertical", command=self.listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.listbox.config(yscrollcommand=scrollbar.set)

        self.hien_thi_danh_sach(self.danh_sach_sp)

    def xu_ly_them(self):
        ma = self.entry_ma.get().strip()
        ten = self.entry_ten.get().strip()
        gia = self.entry_gia.get().strip()
        soluong = self.entry_soluong.get().strip()

        if not ma or not ten or not gia or not soluong:
            messagebox.showerror("Lỗi", "Mã SP và Tên SP không được để trống!")
            return

        try:
            gia = int(gia)
            if gia < 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Lỗi", "Giá sản phẩm phải là một số hợp lệ (>= 0)!")
            return

        try:
            soluong = int(soluong)
            if soluong < 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Lỗi", "Số lượng sản phẩm phải là số nguyên hợp lệ (>= 0)!")
            return

        them_san_pham(self.danh_sach_sp, ma, ten, gia, soluong)
        self.hien_thi_danh_sach(self.danh_sach_sp)

        self.entry_ma.delete(0, tk.END)
        self.entry_ten.delete(0, tk.END)
        self.entry_gia.delete(0, tk.END)
        self.entry_soluong.delete(0, tk.END)
        messagebox.showinfo("Thành công", "Đã thêm sản phẩm mới thành công!")

    def hien_thi_danh_sach(self, ds):
        self.listbox.delete(0, tk.END)
        for sp in ds:

            dong = f"{sp['MaSP']} - {sp['TenSP']} - {sp['Gia']:,.0f}đ - SL: {sp['SoLuong']}"
            self.listbox.insert(tk.END, dong)

    def xu_ly_tim_kiem(self):
        tu_khoa = self.entry_search.get().strip()
        if not tu_khoa:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập từ khóa cần tìm!")
            return
        ket_qua = tim_kiem_theo_ten(self.danh_sach_sp, tu_khoa)
        self.hien_thi_danh_sach(ket_qua)

    def hien_thi_tat_ca(self):
        self.entry_search.delete(0, tk.END)
        self.hien_thi_danh_sach(self.danh_sach_sp)

    def xem_tong_ton_kho(self):
        tong_tien = tong_gia_tri_ton_kho(self.danh_sach_sp)
        messagebox.showinfo("Tổng giá trị tồn kho", f"Tổng giá trị tồn kho hiện tại: {tong_tien:,.0f}đ")


if __name__ == "__main__":
    app = QuanLySanPham()
    app.mainloop()