import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_window = uic.loadUiType('./poster.ui')[0] #Qt디자인에서 만든ui 불러오는 코드

class Exam(QWidget, form_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_wc.clicked.connect(self.btn_wc_clicked_slot)
        self.btn_sleep.clicked.connect(self.btn_wc_clicked_slot)
        self.btn_toy.clicked.connect(self.btn_wc_clicked_slot)
        self.btn_black.clicked.connect(self.btn_wc_clicked_slot)

        # self.btn_sleep.clicked.connect(self.btn_sleep_clicked_slot)
        # self.btn_toy.clicked.connect(self.btn_toy_clicked_slot)
        # self.btn_black.clicked.connect(self.btn_black_clicked_slot)

    def btn_wc_clicked_slot(self):
        btn = self.sender() #어떤버튼눌렀는지 확인하는 코드
        self.lbl_wc.hide()
        self.lbl_sleep.hide()
        self.lbl_toy.hide()
        self.lbl_black.hide()
        if btn.objectName() == 'btn_wc':self.lbl_wc.show()
        elif btn.objectName() == 'btn_sleep':self.lbl_sleep.show()
        elif btn.objectName() == 'btn_toy':self.lbl_toy.show()
        elif btn.objectName() == 'btn_black':self.lbl_black.show()
        ##좀더 간결한 코드 구조

    #     # self.lbl_wc.show()
    #
    # def btn_sleep_clicked_slot(self):
    #
    #     self.lbl_wc.hide()
    #     self.lbl_sleep.hide()
    #     self.lbl_toy.hide()
    #     self.lbl_black.hide()
    #     self.lbl_sleep.show()
    #
    # def btn_toy_clicked_slot(self):
    #     self.lbl_wc.hide()
    #     self.lbl_sleep.hide()
    #     self.lbl_toy.hide()
    #     self.lbl_black.hide()
    #     self.lbl_toy.show()
    #
    # def btn_black_clicked_slot(self):
    #     self.lbl_wc.hide()
    #     self.lbl_sleep.hide()
    #     self.lbl_toy.hide()
    #     self.lbl_black.hide()
    #     self.lbl_black.show()


if __name__=='__main__':
    app = QApplication(sys.argv)
    mainWindow = Exam()
    mainWindow.show()
    sys.exit(app.exec_())   #프로그램종료