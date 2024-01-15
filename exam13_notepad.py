import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_window = uic.loadUiType('./qt_notepad.ui')[0] #Qt디자인에서 만든ui 불러오는 코드

class Exam(QMainWindow, form_window):
## 클래스 작성
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #File
        self.edited_flag = False
        self.path = ['제목 없음','']
        self.title = self.path[0] + " - Qt Note Pad"
        self.setWindowTitle(self.title)
        self.actionSave_as.triggered.connect(self.action_save_as_slot)  #save as 다른이름으로 저장
        self.actionSave.triggered.connect(self.action_save_slot)
        self.actionOpen.triggered.connect(self.action_open_slot)
        self.actionNew.triggered.connect(self.action_new_slot)
        self.actionExit.triggered.connect(self.action_exit_slot)

        #Edit
        self.actionUndo.triggered.connect(self.plainTextEdit.undo)
        self.actionCut.triggered.connect(self.plainTextEdit.cut)
        self.actionCopy.triggered.connect(self.plainTextEdit.copy)
        self.actionPaste.triggered.connect(self.plainTextEdit.paste)
        self.actionDelete.triggered.connect(self.plainTextEdit.cut)

        self.actionFont.triggered.connect(self.action_font_slot)
        self.actionAbout.triggered.connect(self.action_about_slot)

        self.plainTextEdit.textChanged.connect(self.text_changed_slot)

        self.statusbar.showMessage(self.path[0])    ##메모장 하단부 상태바(statusbar)에 상태표시

    def action_about_slot(self):
        QMessageBox.about(self,
                          'PyQt Notepad',
                          '''만든이: 김도영 \n\r버전정보 : 1.0.0''')

    def action_font_slot(self):
        font = QFontDialog.getFont()
        print(font)
        if font[1]:
            self.plainTextEdit.setFont(font[0])


    def action_exit_slot(self):
        if self.edited_flag:
            ## QMessageBox.question - 메세지박스에 퀘스천 마크 나옴
            ans = QMessageBox.question(self,'저장하기', '저장할까요?',
                                       QMessageBox.No | QMessageBox.Cancel | QMessageBox.Yes,
                                        QMessageBox.Yes) ## 위 세가지 or연산은 메세지 박스의 yes,no,cancel 한번더 쓴 Yes는 yes박스에 선택
            if ans == QMessageBox.Yes:
                if self.action_save_slot():
                    return

            elif ans == QMessageBox.Cancel:
                return
        self.close()


    def set_title(self):
        self.title = self.path[0].split('/')[-1] + " - Qt Note Pad"
        self.setWindowTitle(self.title)
        self.edited_flag = False
        self.statusbar.showMessage(self.path[0])


    def text_changed_slot(self):
        self.edited_flag = True
        self.setWindowTitle('*'+self.title)
        print(self.edited_flag)

    def action_new_slot(self):
        if self.edited_flag:
            ## QMessageBox.question - 메세지박스에 퀘스천 마크 나옴
            ans = QMessageBox.question(self,'저장하기', '저장할까요?',
                                       QMessageBox.No | QMessageBox.Cancel | QMessageBox.Yes,
                                        QMessageBox.Yes) ## 위 세가지 or연산은 메세지 박스의 yes,no,cancel 한번더 쓴 Yes는 yes박스에 선택
            if ans == QMessageBox.Yes:
                if self.action_save_slot():
                    return

            elif ans == QMessageBox.Cancel:
                return

        self.plainTextEdit.setPlainText('')
        self.path = ('제목없음','')
        self.set_title()

    def action_open_slot(self):
        if self.edited_flag:
            ans = QMessageBox.question(self, '저장하기', '저장할까요?',
                                       QMessageBox.No | QMessageBox.Cancel | QMessageBox.Yes,
                                       QMessageBox.Yes)  ## 위 세가지 or연산은 메세지 박스의 yes,no,cancel 한번더 쓴 Yes는 yes박스에 선택
            if ans == QMessageBox.Yes:
                self.action_save_slot()
            elif ans == QMessageBox.No:
                pass
            elif ans ==QMessageBox.Cancel:
                return  ##pass와 return은 안해도 됨
        old_path = self.path
        self.path = QFileDialog.getOpenFileName(
            self, 'Open file', '', 'Text File(*.txt);;Python File(*.py);;All File(*.*)')
        if self.path[0] != '':
            with open(self.path[0],'r') as f:        ## with문 - 파일 오픈할때 함께사용
                str_read = f.read()
            self.plainTextEdit.setPlainText(str_read)
            self.set_title()

        else: self.path = old_path
    def action_save_slot(self):
        if self.path[0] != '제목없음':
            with open(self.path[0],'w') as f:
                f.write(self.planTextEdit.toPlanText())
            self.edited_flag = False
            self.set_title()
        else:
            return self.action_save_as_slot()


    def action_save_as_slot(self): #save as버튼 눌렀을때 작동
        old_path = self.path
        self.path = QFileDialog.getSaveFileName(
            self, 'Save file','', 'Text Files(*.txt);;Python Files(*.py);;All Files(*.*)')
        print(self.path)
        if self.path[0] != '':
            with open(self.path[0],'w') as f:
                f.write(self.plainTextEdit.toPlainText())
            self.edited_flag = False
            print(self.edited_flag)
            self.set_title()
            return 0
        else:
            self.path = old_path
            return 1



if __name__=='__main__':
    app = QApplication(sys.argv)
    mainWindow = Exam()
    mainWindow.show()
    sys.exit(app.exec_())   #프로그램종료