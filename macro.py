import sys
# GUI
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

# WEB
from selenium import webdriver
from selenium.webdriver.common.by import By


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 기본설정
        self.setWindowTitle('My First Application')
        self.move(300, 300)
        self.resize(400, 200)
        # self.setGeometry(300, 300, 300, 200) : move + resize
        
        # 시작버튼
        btn = QPushButton('시작', self)
        btn.move(240, 170)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(self.startInterpark)

        # 종료버튼
        btn2 = QPushButton('종료', self)
        btn2.move(320, 170)
        btn2.resize(btn2.sizeHint())
        btn2.clicked.connect(QCoreApplication.instance().quit)

        # 아이콘
        self.setWindowIcon(QIcon('web.png')) 

        # 창 띄우기
        self.show()

        

    # 인터파크
    def startInterpark(self):
        driver = webdriver.Chrome('C:\chromedriver.exe')
        # 사이즈조절
        driver.set_window_size(1400, 1000)  # (가로, 세로)
        driver.get('https://ticket.interpark.com/Gate/TPLogin.asp') # 페이지 이동

    # 멜론티켓
    def startMelon(self):
        driver = webdriver.Chrome('C:\chromedriver.exe')
        # 사이즈조절
        driver.set_window_size(1400, 1000)  # (가로, 세로)
        driver.get('https://ticket.interpark.com/Gate/TPLogin.asp') # 페이지 이동

    # YES24
    def startYes24(self):
        driver = webdriver.Chrome('C:\chromedriver.exe')
        # 사이즈조절
        driver.set_window_size(1400, 1000)  # (가로, 세로)
        driver.get('https://ticket.interpark.com/Gate/TPLogin.asp') # 페이지 이동

    # 세종
    def startSejong(self):
        driver = webdriver.Chrome('C:\chromedriver.exe')
        # 사이즈조절
        driver.set_window_size(1400, 1000)  # (가로, 세로)
        driver.get('https://ticket.interpark.com/Gate/TPLogin.asp') # 페이지 이동



if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())