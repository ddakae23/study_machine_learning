import sys
from PIL import Image
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5 import uic
import numpy as np
from tensorflow.keras.models import load_model
import cv2
import time

form_window = uic.loadUiType('./cat_and_dog.ui')[0] #Qt디자인에서 만든ui 불러오는 코드

class Exam(QWidget, form_window):
#Exam 클래스를 정의 이 클래스는 PyQt5의 QWidget 클래스를 상속하고, UI를 로드한 form_window 클래스를 상속합니다.
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.model = load_model('.\cat_and_dog_0.814.h5')   ##

        self.btn_open.clicked.connect(self.btn_clicked_slot)    ##버튼 불러오는 코드

    def btn_clicked_slot(self): ##버튼 함수
        capture = cv2.VideoCapture(0)
        capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        flag = True

        while flag:
            v, frame = capture.read() ##연결한 웹캠 불러오는 코드
            if (v):
                # cv2.imshow('VideoFrame', frame)
                cv2.imwrite('./capture.png', frame)
                ## 웹캠으로 프레임 캡쳐한 이미지를 capture.png파일에 저장하여 라벨위젯
            # time.sleep(0.01)
            print(v)
            key = cv2.waitKey(50)  ## 키 입력 기다리는 코드
            if key == 27:  ## 27번키 입력시 False / 27번키 아스키코드 Esc키
                flag = False    ##Esc눌렀을때 나가는 코드 / break 도 가능


            pixmap = QPixmap('./capture.png')
            self.lbl_image.setPixmap(pixmap)    ##32번줄 표시하는 코드

            try:
                img = Image.open('./capture.png')
                img = img.convert('RGB')
                img = img.resize((64, 64))
                data = np.asarray(img)
                data = data / 255
                data = data.reshape(1, 64, 64, 3)

                pred = self.model.predict(data)
                print(pred)
                if pred < 0.5:
                    self.label_result.setText('고양이입니다.')
                else:
                    self.label_result.setText('강아지입니다.')
            except:
                print('error')

if __name__=='__main__':
    app = QApplication(sys.argv)
    mainWindow = Exam()
    mainWindow.show()
    sys.exit(app.exec_())   #프로그램종료



# capture = cv2.VideoCapture(0)
# capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# capture.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
# flag = True
# while flag:
#     v, frame = capture.read()
#     if(v):
#         cv2.imshow('VideoFrame',frame)
#         cv2.imwrite('./capture.png', frame)
#     # time.sleep(0.01)
#     print(v)
#     key = cv2.waitKey(50)   ## 키 입력 받는거
#     if key == 27:           ## 27번키 입력시 False / 27번키 아스키코드 Esc키
#         flag = False
#
#     try:
#         img = Image.open('./capture.png')
#         img = img.convert('RGB')
#         img = img.resize((64, 64))
#         data = np.asarray(img)
#         data = data / 255
#         data = data.reshape(1, 64, 64, 3)
#
#         pred = model.predict(data)
#         print(pred)
#         if pred < 0.5:
#             print('고양이입니다.')
#         else:
#             print('강아지입니다.')
#     except:
#         print('error')
