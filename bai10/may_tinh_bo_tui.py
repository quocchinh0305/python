import sys
import os
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget


class MayTinh(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("may_tinh_bo_tui.ui", self)
        cac_nut_so = [
            self.btn_0, self.btn_1, self.btn_2, self.btn_3, self.btn_4,
            self.btn_5, self.btn_6, self.btn_7, self.btn_8, self.btn_9
        ]
        for nut in cac_nut_so:
            nut.clicked.connect(self.nhap_so)

        cac_nut_phep_tinh = [self.btn_cong, self.btn_tru, self.btn_nhan, self.btn_chia]
        for nut in cac_nut_phep_tinh:
            nut.clicked.connect(self.nhap_phep_tinh)

        self.btn_xoa.clicked.connect(self.xoa_man_hinh)
        self.btn_bang.clicked.connect(self.tinh_ket_qua)

    def nhap_so(self):
        nut_duoc_bam = self.sender()
        chuoi_hien_tai = self.man_hinh.text()
        self.man_hinh.setText(chuoi_hien_tai + nut_duoc_bam.text())

    def nhap_phep_tinh(self):
        nut_duoc_bam = self.sender()
        chuoi_hien_tai = self.man_hinh.text()

        if chuoi_hien_tai and chuoi_hien_tai[-1] not in "+-*/":
            self.man_hinh.setText(chuoi_hien_tai + nut_duoc_bam.text())

    def xoa_man_hinh(self):
        self.man_hinh.clear()

    def tinh_ket_qua(self):
        bieu_thuc = self.man_hinh.text()
        try:
            ket_qua = eval(bieu_thuc)
            self.man_hinh.setText(str(ket_qua))
        except Exception:
            self.man_hinh.setText("Lỗi")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    cua_so = MayTinh()
    cua_so.show()
    sys.exit(app.exec_())