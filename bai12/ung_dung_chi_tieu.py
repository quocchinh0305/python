import tkinter as tk
from tkinter import ttk, messagebox
import datetime
import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

import csdl_chi_tieu as db

DANH_SACH_DANH_MUC = ["Ăn uống", "Nhà cửa", "Đi lại", "Học tập", "Giải trí", "Mua sắm", "Khác"]
DANH_SACH_TRANG_THAI = ["Chưa thanh toán", "Đã thanh toán"]


class UngDungChiTieu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ứng dụng Quản lý Chi tiêu cá nhân")
        self.geometry("720x560")
        self.resizable(False, False)
        db.tao_bang_neu_chua_co()
        self.khoi_tao_giao_dien()
        self.tai_lai_danh_sach()

    def tai_lai_danh_sach(self):
        self.listbox_chi.delete(0, tk.END)
        self.danh_sach_hien_tai = db.lay_toan_bo_chi_tieu()
        for item in self.danh_sach_hien_tai:
            id_chi, ngay, danh_muc, so_tien, trang_thai, mo_ta = item
            chuoi_hien_thi = f"[{ngay}] {danh_muc:12} | {so_tien:12,.0f} VNĐ | {trang_thai:15} | {mo_ta}"
            self.listbox_chi.insert(tk.END, chuoi_hien_thi)

    def xu_ly_them(self):
        ngay = self.o_nhap_ngay.get().strip()
        danh_muc = self.chon_danh_muc.get()
        chuoi_so_tien = self.o_nhap_so_tien.get().strip().replace(",", "").replace(".", "")
        trang_thai = self.chon_trang_thai.get()
        mo_ta = self.o_nhap_mo_ta.get().strip()

        if not ngay or not chuoi_so_tien:
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ Ngày và Số tiền.")
            return
        try:
            so_tien = float(chuoi_so_tien)
            if so_tien <= 0:
                raise ValueError()
        except ValueError:
            messagebox.showerror("Lỗi", "Số tiền phải là một số hợp lệ lớn hơn 0.")
            return

        db.them_khoan_chi(ngay, danh_muc, so_tien, trang_thai, mo_ta)
        self.o_nhap_so_tien.delete(0, tk.END)
        self.o_nhap_mo_ta.delete(0, tk.END)
        self.chon_trang_thai.current(0)
        self.tai_lai_danh_sach()
        messagebox.showinfo("Thành công", "Đã thêm khoản chi tiêu mới.")

    def xu_ly_doi_trang_thai(self):
        lua_chon = self.listbox_chi.curselection()
        if not lua_chon:
            messagebox.showerror("Lỗi", "Vui lòng chọn một khoản chi trong danh sách để đổi trạng thái.")
            return
        id_chi = self.danh_sach_hien_tai[lua_chon[0]][0]
        trang_thai_hien_tai = self.danh_sach_hien_tai[lua_chon[0]][4]
        trang_thai_moi = "Đã thanh toán" if trang_thai_hien_tai == "Chưa thanh toán" else "Chưa thanh toán"
        db.cap_nhat_trang_thai(id_chi, trang_thai_moi)
        self.tai_lai_danh_sach()

    def xu_ly_xoa(self):
        lua_chon = self.listbox_chi.curselection()
        if not lua_chon:
            messagebox.showerror("Lỗi", "Vui lòng chọn một khoản chi trong danh sách để xóa.")
            return
        id_chi = self.danh_sach_hien_tai[lua_chon[0]][0]
        db.xoa_khoan_chi(id_chi)
        self.tai_lai_danh_sach()
        messagebox.showinfo("Thành công", "Đã xóa khoản chi tiêu.")

    def xu_ly_thong_ke(self):
        du_lieu = db.thong_ke_theo_danh_muc()
        if not du_lieu:
            messagebox.showinfo("Thông báo", "Chưa có dữ liệu chi tiêu 'Đã thanh toán' để thống kê.")
            return
        cac_danh_muc = [dong[0] for dong in du_lieu]
        tong_tien = [dong[1] for dong in du_lieu]
        bang_mau = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEEAD', '#D4A5A5', '#9B59B6', '#34495E']
        plt.figure(figsize=(7, 4.5))
        plt.bar(cac_danh_muc, tong_tien, color=bang_mau[:len(cac_danh_muc)])
        plt.title("Thống kê tổng chi tiêu theo danh mục (Đã thanh toán)")
        plt.xlabel("Danh mục")
        plt.ylabel("Tổng số tiền (VNĐ)")
        plt.xticks(rotation=15)
        plt.tight_layout()
        plt.show()

    def khoi_tao_giao_dien(self):
        khung_nhap = tk.LabelFrame(self, text=" Thêm khoản chi tiêu mới ", padx=10, pady=10)
        khung_nhap.pack(pady=10, padx=10, fill="x")

        tk.Label(khung_nhap, text="Ngày (YYYY-MM-DD):").grid(row=0, column=0, sticky="w", pady=5)
        self.o_nhap_ngay = tk.Entry(khung_nhap, width=30)
        self.o_nhap_ngay.grid(row=0, column=1, padx=10, pady=5)
        self.o_nhap_ngay.insert(0, datetime.date.today().strftime("%Y-%m-%d"))

        tk.Label(khung_nhap, text="Danh mục:").grid(row=1, column=0, sticky="w", pady=5)
        self.chon_danh_muc = ttk.Combobox(khung_nhap, values=DANH_SACH_DANH_MUC, width=27, state="readonly")
        self.chon_danh_muc.current(0)
        self.chon_danh_muc.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(khung_nhap, text="Số tiền (VNĐ):").grid(row=2, column=0, sticky="w", pady=5)
        self.o_nhap_so_tien = tk.Entry(khung_nhap, width=30)
        self.o_nhap_so_tien.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(khung_nhap, text="Trạng thái:").grid(row=3, column=0, sticky="w", pady=5)
        self.chon_trang_thai = ttk.Combobox(khung_nhap, values=DANH_SACH_TRANG_THAI, width=27, state="readonly")
        self.chon_trang_thai.current(0)
        self.chon_trang_thai.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(khung_nhap, text="Mô tả / Ghi chú:").grid(row=4, column=0, sticky="w", pady=5)
        self.o_nhap_mo_ta = tk.Entry(khung_nhap, width=30)
        self.o_nhap_mo_ta.grid(row=4, column=1, padx=10, pady=5)

        tk.Button(khung_nhap, text="Thêm khoản chi", bg="#4CAF50", fg="white", font=("Arial", 9, "bold"), command=self.xu_ly_them).grid(
            row=5, column=0, columnspan=2, pady=10
        )

        khung_danh_sach = tk.LabelFrame(self, text=" Lịch sử chi tiêu ", padx=10, pady=10)
        khung_danh_sach.pack(pady=5, padx=10, fill="both", expand=True)

        self.listbox_chi = tk.Listbox(khung_danh_sach, width=95, height=10, font=("Courier New", 9))
        self.listbox_chi.pack(side="left", fill="both", expand=True)

        thanh_cuon = tk.Scrollbar(khung_danh_sach, orient="vertical", command=self.listbox_chi.yview)
        thanh_cuon.pack(side="right", fill="y")
        self.listbox_chi.config(yscrollcommand=thanh_cuon.set)

        khung_nut = tk.Frame(self)
        khung_nut.pack(pady=10)

        tk.Button(khung_nut, text="Đổi trạng thái (Đã/Chưa)", bg="#FF9800", fg="white", font=("Arial", 9, "bold"), command=self.xu_ly_doi_trang_thai).grid(row=0, column=0, padx=8)
        tk.Button(khung_nut, text="Xóa khoản đã chọn", bg="#f44336", fg="white", font=("Arial", 9, "bold"), command=self.xu_ly_xoa).grid(row=0, column=1, padx=8)
        tk.Button(khung_nut, text="Thống kê theo danh mục", bg="#2196F3", fg="white", font=("Arial", 9, "bold"), command=self.xu_ly_thong_ke).grid(row=0, column=2, padx=8)

if __name__ == "__main__":
    ung_dung = UngDungChiTieu()
    ung_dung.mainloop()