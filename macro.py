import sys
# GUI
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

# WEB
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

import easyocr
import time
import traceback
import js2py

driver = webdriver.Chrome('C:\chromedriver.exe')
driver.set_window_size(800, 1000)  # (가로, 세로)

step = 0

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 기본설정
        self.setWindowTitle('My First Application')
        self.move(1400, 300)
        self.resize(400, 200)
        # self.setGeometry(300, 300, 300, 200) : move + resize

        #  버튼
        btn = QPushButton('티켓팅이동', self)
        btn.move(80, 100)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(self.gotoTicketing)

        #  버튼
        btn = QPushButton('재시작', self)
        btn.move(80, 170)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(self.reStart)
        
        # 로그인 버튼
        btn = QPushButton('로그인', self)
        btn.move(160, 170)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(self.loginInterpark)

         # 시작 버튼
        btn = QPushButton('시작', self)
        btn.move(240, 170)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(self.macroManager)

        # 종료 버튼
        btn2 = QPushButton('종료', self)
        btn2.move(320, 170)
        btn2.resize(btn2.sizeHint())
        btn2.clicked.connect(QCoreApplication.instance().quit)

        # 아이콘
        self.setWindowIcon(QIcon('web.png')) 

        # 창 띄우기
        self.show()

    # 재시작
    def reStart(self):
        global driver
        driver = webdriver.Chrome('C:\chromedriver.exe')
        driver.set_window_size(800, 1000)  # (가로, 세로)

        global step
        step = 0

    # 인터파크 로그인
    def loginInterpark(self):
        try :
            driver.get('https://ticket.interpark.com/Gate/TPLogin.asp') # 페이지 이동

            driver.switch_to.frame(driver.find_element(By.XPATH, "//div[@class='leftLoginBox']/iframe[@title='login']"))
            userId = driver.find_element(By.ID, 'userId')
            userId.send_keys('won5854') # 로그인 할 계정 id
            userPwd = driver.find_element(By.ID, 'userPwd')
            userPwd.send_keys('skfkrh@816') # 로그인 할 계정의 패스워드
            time.sleep(5)
            userPwd.send_keys(Keys.ENTER)
            # driver.get('http://ticket.interpark.com/Ticket/Goods/GoodsInfo.asp?GoodsCode=' + '22004761')
            self.gotoTicketing()
        
        except:
            traceback.print_exc()

    def gotoTicketing(self):
        driver.get('http://ticket.interpark.com/Ticket/Goods/GoodsInfo.asp?GoodsCode=' + '22004761')
        
        global step
        step = 0

    # 매크로 매니저
    def macroManager(self):
        print("macroManager ::: " + str(step))
        # 예매하기
        if step == 0 :
            self.startInterpark()
        # 회차선택
        elif step == 1 :
            self.selDayHoicha()
        # 좌석선택
        elif step == 2 :
            self.selSeat()


    # 인터파크 예매시작
    def startInterpark(self):
        try :
            # 예매하기 버튼 클릭
            driver.find_element(By.XPATH, "//div[@class='sideBtnWrap']/a[@class='sideBtn is-primary']").click()

            global step
            step = 1

            # alert 확인버튼 누른 후 문자입력
            # time.sleep(5)

            # 예매안내가 팝업이 뜨면 닫기. ( ticketingInfo_check : True, False )
            # ticketingInfo_check = self.check_exists_by_element(By.XPATH, "//div[@class='layerWrap']/div[@class='titleArea']/a[@class='closeBtn']")
            # if ticketingInfo_check:
            #    driver.find_element(By.XPATH, "//div[@class='layerWrap']/div[@class='titleArea']/a[@class='closeBtn']").click()
        
        except:
            traceback.print_exc()

    # 회차선택
    def selDayHoicha(self):
        print("selDayHoicha")

        try :
            # 테스트 회차 2022년 07월 15일 1회차
            arr1 = [['20220715', 1]]
            
            # 예매하기 눌러서 새창이 뜨면 포커스를 새창으로 변경
            driver.switch_to.window(driver.window_handles[1])
            driver.get_window_position(driver.window_handles[1])

            driver.switch_to.frame(driver.find_element(By.XPATH, "//div[@id='divBookSeat']/iframe[@id='ifrmSeat']"))

            selDay = Select(driver.find_element(By.ID, 'PlayDate'))
            selHoiCha = Select(driver.find_element(By.ID, 'PlaySeq'))

            selDay.select_by_value(arr1[0][0])
            time.sleep(0.5)
            selHoiCha.select_by_index(arr1[0][1])

            # driver.switch_to.default_content()
            
            global step
            step = 2
            self.macroManager()

        except:
            traceback.print_exc()

    # 좌석선택
    def selSeat(self):
        print("selSeat")
        
        try :
            driver.switch_to.frame(driver.find_element(By.XPATH, "//*[@id='ifrmSeatDetail']"))
            time.sleep(3)
            seats = driver.find_elements(By.XPATH, "//*[@id='TmgsTable']/tbody/tr/td/img[contains(@title, '1층') and contains(@title, 'S석')]")
            # seats2 = driver.find_elements_by_xpath("//*[@id='TmgsTable']/tbody/tr/td/img[@class='stySeat' and contains(@title, '1층') and contains(@title, 'S석')]")

            # # element.get_attribute("attribute name")

            for item in seats:
                print(item.get_attribute("title"))

            seats.sort(key=lambda e: e.get_attribute("title"))

            for item in seats:
                print(item.get_attribute("title"))

            # print(seats)
            print(len(seats))

            # arr = [['3', '1층', 'A열', '194', '101']
            #     ,['3', '1층', 'A열', '195', '101']
            #     ,['3', '1층', 'A열', '196', '101']
            #     ,['3', '1층', 'A열', '197', '101']
            # ]

            # scriptJS='''
            #     function javascriptCode(a,b,c,d,e) {
            #         SelectSeat('SID2', a, b, c, d, e);
            #     }
            # '''

            # fnJs = js2py.eval_js(scriptJS)

            # for item in arr:
            #     # 등급, 층, 열, 좌석번호, 구역
            #     fnJs(item[0], item[1], item[2], item[3], item[4] )

            global step
            step = 3
            self.macroManager()

        
        except:
            traceback.print_exc()


    def easyocrChar(self):
        print("easyocrChar")
         # 문자열 인식
        # capchaPng = driver.find_element(By.XPATH, "//*[@id='oCaptchaFrame']") # 입력해야될 문자 이미지 캡쳐하기. iframe
        # reader = easyocr.Reader(['en']) # easyocr 이미지내 인식할 언어 지정
        # result = reader.readtext(capchaPng.screenshot_as_png, detail=0) # 캡쳐한 이미지에서 문자열 인식하기

        # print(result[0])

        # # 이미지에 점과 직선이 포함되어있어서 문자 인식 데이터 수동 보정
        # capchaValue = result[0].replace(' ', '').replace('$', 'S').replace(',', '')\
        #     .replace(':', '').replace('.', '').replace('+', 'T').replace("'", '').replace('`', '')\
        #     .replace('e', 'Q').replace('3', 'S').replace('€', 'C').replace('{', '').replace('-', '')

        # print(capchaValue)
        # chapchaText = driver.find_element(By.ID, 'oCheckCaptcha')
        # chapchaText.send_keys(capchaValue)

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