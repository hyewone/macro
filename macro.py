import sys
# GUI
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

# WEB
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 문자인식
import easyocr

driver = webdriver.Chrome('C:\chromedriver.exe')

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
        
        # 로그인 버튼
        btn = QPushButton('로그인', self)
        btn.move(160, 170)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(self.loginInterpark)

         # 시작 버튼
        btn = QPushButton('시작', self)
        btn.move(240, 170)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(self.startInterpark)

        # 종료 버튼
        btn2 = QPushButton('종료', self)
        btn2.move(320, 170)
        btn2.resize(btn2.sizeHint())
        btn2.clicked.connect(QCoreApplication.instance().quit)

        # 아이콘
        self.setWindowIcon(QIcon('web.png')) 

        # 창 띄우기
        self.show()

    # 인터파크 로그인
    def loginInterpark(self):
        driver.set_window_size(800, 1000)  # (가로, 세로)
        driver.get('https://ticket.interpark.com/Gate/TPLogin.asp') # 페이지 이동

        driver.switch_to.frame(driver.find_element(By.XPATH, "//div[@class='leftLoginBox']/iframe[@title='login']"))
        userId = driver.find_element(By.ID, 'userId')
        userId.send_keys('won5854') # 로그인 할 계정 id
        userPwd = driver.find_element(By.ID, 'userPwd')
        userPwd.send_keys('skfkrh@816') # 로그인 할 계정의 패스워드

        # 문자열 인식
        capchaPng = driver.find_element(By.XPATH, "//*[@id='oCaptchaFrame']") # 입력해야될 문자 이미지 캡쳐하기. iframe
        reader = easyocr.Reader(['en']) # easyocr 이미지내 인식할 언어 지정
        result = reader.readtext(capchaPng.screenshot_as_png, detail=0) # 캡쳐한 이미지에서 문자열 인식하기

        print(result[0])

        # 이미지에 점과 직선이 포함되어있어서 문자 인식 데이터 수동 보정
        capchaValue = result[0].replace(' ', '').replace('$', 'S').replace(',', '')\
            .replace(':', '').replace('.', '').replace('+', 'T').replace("'", '').replace('`', '')\
            .replace('e', 'Q').replace('3', 'S').replace('€', 'C').replace('{', '').replace('-', '')

        print(capchaValue)
        chapchaText = driver.find_element(By.ID, 'oCheckCaptcha')
        chapchaText.send_keys(capchaValue)
        userPwd.send_keys(Keys.ENTER)

    # 인터파크 예매시작
    def startInterpark(self):
        driver.get('http://ticket.interpark.com/Ticket/Goods/GoodsInfo.asp?GoodsCode=' + '22004761')
        # 예매하기 버튼 클릭
        driver.find_element(By.XPATH, "//div[@class='sideBtnWrap']/a[@class='sideBtn is-primary']").click()
        
        # 예매하기 눌러서 새창이 뜨면 포커스를 새창으로 변경
        driver.switch_to.window(driver.window_handles[1])
        driver.get_window_position(driver.window_handles[1])

        # 예매안내가 팝업이 뜨면 닫기. ( ticketingInfo_check : True, False )
        ticketingInfo_check = self.check_exists_by_element(By.XPATH, "//div[@class='layerWrap']/div[@class='titleArea']/a[@class='closeBtn']")
        if ticketingInfo_check:
           driver.find_element(By.XPATH, "//div[@class='layerWrap']/div[@class='titleArea']/a[@class='closeBtn']").click()

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