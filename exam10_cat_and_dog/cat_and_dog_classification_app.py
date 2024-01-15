import sys
from PIL import Image
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
import numpy as np
from tensorflow.keras.models import load_model
from PyQt5 import uic

form_window = uic.loadUiType('./cat_and_dog.ui')[0] #Qt디자인에서 만든ui 불러오는 코드

class Exam(QWidget, form_window):
    def __init__(self):
        super().__init__()
        self.setFixedWidth(600)
        self.setFixedHeight(600)
        self.setupUi(self)
        self.btn_open.clicked.connect(self.btn_clicked_slot)
        model_path='./cat_and_dog_0.814.h5'
        self.model=load_model(model_path)
        self.path=('../datasets/cat_dog/test/cat_cute.jpg','')
        pixmap = QPixmap(self.path[0])
        self.lbl_image.setPixmap(pixmap)


    def btn_clicked_slot(self):

        old_path = self.path
        self.path=QFileDialog.getOpenFileName(self, 'Open file',
                                    '../datasets/cat_dog', 'image Files(*.jpg; *.png);;All Files(*.*)')
        if self.path[0]=='':
            self.path=old_path
        print(self.path)
        pixmap = QPixmap(self.path[0])
        self.lbl_image.setPixmap(pixmap)
        try:
            img = Image.open(self.path[0])
            img = img.convert('RGB')
            img = img.resize((64, 64))
            data = np.asarray(img)
            data = data / 255
            data = data.reshape(1, 64, 64, 3)

            pred = self.model.predict(data)
            print(pred)
            if pred < 0.5:
                self.label_result.setText('고양이입니다.')
            else: self.label_result.setText('강아지입니다.')
        except:
            print('error : {}'.format(self.path[0]))


if __name__=='__main__':
    app = QApplication(sys.argv)
    mainWindow = Exam()
    mainWindow.show()
    sys.exit(app.exec_())   #프로그램종료