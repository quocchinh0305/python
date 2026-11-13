import pandas as pd
import matplotlib.pyplot as plt
def main():
 try:
        df=pd.read_csv("sanpham.csv")
 except FileNotFoundError:
    print("Không tìm thấy file sanpham.csv nào cả")
    return
 print("Đọc dữ liệu từ file")
 print(df)
 tong_so_san_pham=len(df)
 gia_trung_binh=df["Gia"].mean()
 max_row=df.loc[df["Gia"].idxmax()]
 ten_sp_gia_cao_nhat=max_row["TenSP"]
 print(f"Tổng sổ sản phẩm là: {tong_so_san_pham}")
 print(f"Gía trung bình:",gia_trung_binh)
 print(f"Tên sản phẩm giá cao nhất:{ten_sp_gia_cao_nhat}")
 plt.figure(figsize=(10,10))
 plt.bar(df["TenSP"],df["SoLuong"],color="green")
 plt.xlabel("Tên sản pham")
 plt.ylabel("Số lượng tồn kho")
 plt.title("Biểu đồ thể hiện số lượng tồn kho của sản phẩm")
 plt.xticks(rotation=15)
 plt.tight_layout()
 plt.show()
 plt.savefig("bieudo.png")
 plt.close()
 print("-> Đã lưu biểu đồ tồn kho thành công vào file 'bieudo.png'.")
 df_sap_het = df[df["SoLuong"] < 10]
 df_sap_het.to_csv("canh_bao_hang.csv", index=False)
 print("-> Đã xuất danh sách sản phẩm sắp hết hàng (< 10) ra file 'canh_bao_hang.csv'.")
 print("\nNội dung file canh_bao_hang.csv:")
 print(df_sap_het)

if __name__=="__main__":
    main()




