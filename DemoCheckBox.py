# DemoCheckBox.py
import sys
from PyQt5.QtWidgets import *

class DemoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        # (x위치, y위치, 폭, 높이)
        self.setGeometry(800, 200, 300, 300)

        self.checkBox1 = QCheckBox("아이폰", self)
        # (x, y)으로 이동
        self.checkBox1.move(10, 20)
        # (폭, 높이)
        self.checkBox1.resize(150, 30)
        # 슬롯(event) : 체크 박스의 상태가 변경될 경우
        self.checkBox1.stateChanged.connect(self.checkBoxState)

        self.checkBox2 = QCheckBox("안드로이드폰", self)
        # (x, y)으로 이동, 1번 대비 30픽셀 y축 아래 방향으로 이동
        self.checkBox2.move(10, 50)
        self.checkBox2.resize(150, 30)
        self.checkBox2.stateChanged.connect(self.checkBoxState)

        self.checkBox3 = QCheckBox("윈도우폰", self)
        # (x, y)으로 이동, 2번 대비 30픽셀 y축 아래 방향으로 이동
        self.checkBox3.move(10, 80)
        self.checkBox3.resize(150, 30)
        self.checkBox3.stateChanged.connect(self.checkBoxState)

        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)

    def checkBoxState(self):
        msg = ""
        if self.checkBox1.isChecked() == True:
            msg += "아이폰 "
        if self.checkBox2.isChecked() == True:
            msg += "안드로이드폰 "
        if self.checkBox3.isChecked() == True:
            msg += "윈도우폰 "
        self.statusBar.showMessage(msg)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = DemoWindow()
    demoWindow.show()
    app.exec_()