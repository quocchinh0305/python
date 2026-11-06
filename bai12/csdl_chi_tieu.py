import sqlite3

TEN_DB = "chi_tieu.db"

def tao_bang_neu_chua_co():
    conn = sqlite3.connect(TEN_DB)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS chi_tieu (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ngay TEXT,
            danh_muc TEXT,
            so_tien REAL,
            trang_thai TEXT,
            mo_ta TEXT
        )
    ''')
    conn.commit()
    conn.close()

def them_khoan_chi(ngay, danh_muc, so_tien, trang_thai, mo_ta):
    conn = sqlite3.connect(TEN_DB)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO chi_tieu (ngay, danh_muc, so_tien, trang_thai, mo_ta) VALUES (?, ?, ?, ?, ?)",
        (ngay, danh_muc, so_tien, trang_thai, mo_ta)
    )
    conn.commit()
    conn.close()

def lay_toan_bo_chi_tieu():
    conn = sqlite3.connect(TEN_DB)
    cursor = conn.cursor()
    cursor.execute("SELECT id, ngay, danh_muc, so_tien, trang_thai, mo_ta FROM chi_tieu ORDER BY ngay DESC, id DESC")
    ket_qua = cursor.fetchall()
    conn.close()
    return ket_qua

def xoa_khoan_chi(id_chi):
    conn = sqlite3.connect(TEN_DB)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM chi_tieu WHERE id = ?", (id_chi,))
    conn.commit()
    conn.close()

def cap_nhat_trang_thai(id_chi, trang_thai_moi):
    conn = sqlite3.connect(TEN_DB)
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE chi_tieu SET trang_thai = ? WHERE id = ?",
        (trang_thai_moi, id_chi)
    )
    conn.commit()
    conn.close()

def thong_ke_theo_danh_muc():
    conn = sqlite3.connect(TEN_DB)
    cursor = conn.cursor()
    cursor.execute("SELECT danh_muc, SUM(so_tien) FROM chi_tieu WHERE trang_thai = 'Đã thanh toán' GROUP BY danh_muc")
    ket_qua = cursor.fetchall()
    conn.close()
    return ket_qua