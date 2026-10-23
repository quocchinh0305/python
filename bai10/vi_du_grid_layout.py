import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QGridLayout
class VIDUGRIDLAYOUT(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vi du QGridLayout")
        self.resize(300,200)
        layout = QGridLayout()
        layout.addWidget(QLabel("Họ tên: "),0,0)
        layout.addWidget(QLabel("Tuoi"),1,0)
        layout.addWidget(QPushButton("dong y"),2,0)
        layout.addWidget(QPushButton("huy"),2,1)
        self.setLayout(layout)
app=QApplication(sys.argv)
cua_so=VIDUGRIDLAYOUT()
cua_so.show()
sys.exit(app.exec_())