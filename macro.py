import sys
# GUI
from PyQt5.QtWidgets import *
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

g_step = 0
g_wait = 5
g_repeatCnt = 0

### 사용자 변수 ###
# 아이디 ex: won5854, klnsun89
g_id = "won5854"
# 패스워드 ex: skfkrh@816
g_pwd = "skfkrh@816"
# 생년월일
g_birth = "951209"
# 상품번호 ex: 22004761
g_goodsNum = "22004761"
# 날짜 ex: 20220715
g_date = "20220715"
# 회차 ex: 1, 2
g_hoicha = '1'
# 층 ex: 1층
g_floor = "1층"
# 석 ex: S석, VIP석
g_seatGrade = "S석"
# 구역 ex: C열, E열
g_block = "A열"

# 테스트 회차 2022년 07월 15일 1회차
arr1 = [ ['20220715', 1]
        ,['20220719', 1]
        ,['20220720', 2]
        ,['20220722', 2]
        ,['20220724', 1]
        ,['20220726', 1]
        ,['20220727', 2]
        ,['20220729', 1]
        ,['20220731', 2]
        ,['20220802', 1]
        ,['20220803', 2]
        ,['20220805', 2]
        ,['20220807', 1]]

g_date_arr = [   '20220715'
                ,'20220719'
                ,'20220720'
                ,'20220722'
                ,'20220724'
                ,'20220726'
                ,'20220727'
                ,'20220729'
                ,'20220731'
                ,'20220802'
                ,'20220803'
                ,'20220805'
                ,'20220807']
g_hoicah_arr = ['1', '2']
g_floor_arr = ['1층', '2층', '3층']
g_grade_arr = ['VIP석', 'S석', 'A석', 'R석', 'B석']
g_block_arr = ['A열', 'B열', 'C열', 'D열', 'E열']


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 기본설정
        self.setWindowTitle('Macro')
        self.move(1200, 150)
        self.resize(500, 700)

        # 설정저장
        # btn = QPushButton('설정저장', self)
        # btn.setGeometry(380, 10, 40, 25)
        # btn.resize(btn.sizeHint())
        # btn.clicked.connect(self.loginInterpark)

        # ID
        labelId = QLabel('ID:', self)
        labelId.setGeometry(30, 50, 70, 25)
        self.lineEditId = QLineEdit(self)
        self.lineEditId.setGeometry(100, 50, 110, 25)
        self.lineEditId.textEdited.connect(self.changeInputId)

        # PW
        labelPw = QLabel('PW:', self)
        labelPw.setGeometry(250, 50, 70, 25)
        self.lineEditPw = QLineEdit(self)
        self.lineEditPw.setGeometry(320, 50, 110, 25)
        self.lineEditPw.textEdited.connect(self.changeInputPw)

        # -----------------------------------------------

        # 생년월일
        labelBirth = QLabel('생년월일:', self)
        labelBirth.setGeometry(30, 90, 70, 25)
        self.lineEditBirth = QLineEdit(self)
        self.lineEditBirth.setGeometry(100, 90, 110, 25)
        self.lineEditBirth.textEdited.connect(self.changeInputBirth)
        
        label1 = QLabel('---------------------------------------------------', self)
        label1.setGeometry(30, 125, 450, 25)

        # -----------------------------------------------
        
        # 공연번호
        labelNo = QLabel('공연번호:', self)
        labelNo.setGeometry(30, 150, 70, 25)
        self.lineEditNo = QLineEdit(self)
        self.lineEditNo.setGeometry(100, 150, 110, 25)
        self.lineEditNo.textEdited.connect(self.changeInputNo)

        # 공연일자
        labelDate = QLabel('공연일자:', self)
        labelDate.setGeometry(250, 150, 70, 25)
        self.cbDate = QComboBox(self)
        self.cbDate.addItems(g_date_arr)
        self.cbDate.setGeometry(320, 150, 110, 25)
        self.cbDate.currentIndexChanged.connect(self.changeComboDate)

        # -----------------------------------------------
        
        # 공연회차
        labelHoicha = QLabel('공연회차:', self)
        labelHoicha.setGeometry(250, 190, 70, 25)
        self.cbHoicha = QComboBox(self)
        self.cbHoicha.addItems(g_hoicah_arr)
        self.cbHoicha.setGeometry(320, 190, 110, 25)
        self.cbHoicha.currentIndexChanged.connect(self.changeComboHoicha)

        label1 = QLabel('---------------------------------------------------', self)
        label1.setGeometry(30, 225, 450, 25)

        # -----------------------------------------------

        # 좌석층
        labelFoor = QLabel('좌석층:', self)
        labelFoor.setGeometry(30, 250, 70, 25)
        self.cbFoor = QComboBox(self)
        self.cbFoor.addItems(g_floor_arr)
        self.cbFoor.setGeometry(100, 250, 110, 25)
        self.cbFoor.currentIndexChanged.connect(self.changeComboFloor)

        # 좌석등급
        labelGrade = QLabel('좌석등급:', self)
        labelGrade.setGeometry(250, 250, 70, 25)
        self.cbGrade = QComboBox(self)
        self.cbGrade.addItems(g_grade_arr)
        self.cbGrade.setGeometry(320, 250, 110, 25)
        self.cbGrade.currentIndexChanged.connect(self.changeComboGrade)

        # -----------------------------------------------

        # 좌석구역
        labelBlock = QLabel('구역:', self)
        labelBlock.setGeometry(250, 290, 70, 25)
        self.cbBlock = QComboBox(self)
        self.cbBlock.addItems(g_block_arr)
        self.cbBlock.setGeometry(320, 290, 110, 25)
        self.cbBlock.currentIndexChanged.connect(self.changeComboBlock)

        label1 = QLabel('---------------------------------------------------', self)
        label1.setGeometry(30, 325, 450, 25)

        # -----------------------------------------------

        self.lineEditId.setText(g_id)
        self.lineEditPw.setText(g_pwd)
        self.lineEditBirth.setText(g_birth)
        self.lineEditNo.setText(g_goodsNum)
        self.cbDate.setCurrentText(g_date)
        self.cbHoicha.setCurrentText(g_hoicha)
        self.cbFoor.setCurrentText(g_floor)
        self.cbGrade.setCurrentText(g_seatGrade)
        self.cbBlock.setCurrentText(g_block)

        # -----------------------------------------------

        # 1. 로그인
        btn = QPushButton('1. 로그인', self)
        btn.setGeometry(30, 370, 200, 50)
        btn.clicked.connect(self.loginInterpark)

        # 2. 티켓팅 페이지 이동
        btn = QPushButton('2. 티켓팅 이동', self)
        btn.setGeometry(250, 370, 200, 50)
        btn.clicked.connect(self.gotoTicketing)

        # 3. 회차 및 좌석선택
        btn = QPushButton('3. 회차 및 좌석선택', self)
        btn.setGeometry(30, 450, 200, 50)
        btn.clicked.connect(self.selDayHoicha)

        # 4. 좌석단계 좌석 재선택
        btn = QPushButton('4. 좌석 - 좌석 재선택', self)
        btn.setGeometry(250, 450, 200, 50)
        btn.clicked.connect(self.reSelSeatSeat)

        # 5. 결제단계 좌석 재선택
        btn = QPushButton('5. 결제 - 좌석 재선택', self)
        btn.setGeometry(30, 530, 200, 50)
        btn.clicked.connect(self.reSelSeatPay)

        # 6. 좌석선택완료
        btn = QPushButton('6. 좌석선택완료', self)
        btn.setGeometry(250, 530, 200, 50)
        btn.clicked.connect(self.afterProcess)
        
        # 7. 회차 재선택
        btn = QPushButton('7. 회차 재선택', self)
        btn.setGeometry(30, 610, 200, 50)
        btn.clicked.connect(self.selDayHoicha)

         # 8. 재시작
        btn = QPushButton('8. 재시작', self)
        btn.setGeometry(250, 610, 200, 50)
        btn.clicked.connect(self.reStart) 

        # # 종료 버튼
        # btn2 = QPushButton('종료', self)
        # btn2.move(320, 170)
        # btn2.resize(btn2.sizeHint())
        # btn2.clicked.connect(QCoreApplication.instance().quit)

        # 아이콘
        self.setWindowIcon(QIcon('web.png')) 

        # 창 띄우기
        self.show()

    # 재시작
    def reStart(self):
        global driver
        driver = webdriver.Chrome('C:\chromedriver.exe')
        driver.set_window_size(800, 1000)  # (가로, 세로)

        # global g_step
        # g_step = 0

    # 인터파크 로그인
    def loginInterpark(self):
        try :
            driver.get('https://ticket.interpark.com/Gate/TPLogin.asp') # 페이지 이동

            driver.switch_to.frame(driver.find_element(By.XPATH, "//div[@class='leftLoginBox']/iframe[@title='login']"))
            userId = driver.find_element(By.ID, 'userId')
            userId.send_keys(g_id)
            userPwd = driver.find_element(By.ID, 'userPwd')
            userPwd.send_keys(g_pwd) # 로그인 할 계정의 패스워드
            time.sleep(5)
            userPwd.send_keys(Keys.ENTER)
            self.gotoTicketing()
        
        except:
            traceback.print_exc()

    # 상품 티켓팅 페이지 이동
    def gotoTicketing(self):
        # driver.get('http://ticket.interpark.com/Ticket/Goods/GoodsInfo.asp?GoodsCode=' + g_goodsNum)
        try :
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[1])
            # 새로운 화면에서 열리도록 해야하나?
            driver.get('https://poticket.interpark.com/Book/BookSession.asp?GroupCode=' + g_goodsNum +'&Tiki=N&PlayDate=20220715&PlaySeq=046')
        except:
            traceback.print_exc()
        # global g_step
        # g_step = 0
        # g_step = 1

    # 인터파크 예매시작
    def startInterpark(self):
        try :
            # 예매하기 버튼 클릭
            driver.find_element(By.XPATH, "//div[@class='sideBtnWrap']/a[@class='sideBtn is-primary']").click()

            global g_step
            g_step = 1

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
        # print("selDayHoicha")

        try :
            # 예매하기 눌러서 새창이 뜨면 포커스를 새창으로 변경
            # driver.switch_to.window(driver.window_handles[1])
            driver.get_window_position(driver.window_handles[1])

            driver.switch_to.frame(driver.find_element(By.XPATH, "//div[@id='divBookSeat']/iframe[@id='ifrmSeat']"))

            selDay = Select(driver.find_element(By.ID, 'PlayDate'))
            selHoiCha = Select(driver.find_element(By.ID, 'PlaySeq'))

            selDay.select_by_index('0')
            selHoiCha.select_by_index('0')

            selDay.select_by_value(g_date)
            time.sleep(0.5)
            selHoiCha.select_by_index(g_hoicha)
            
            # global g_step
            # g_step = 2
            # self.macroManager()
            self.selSeat()

        except:
            traceback.print_exc()

    # 좌석선택
    def selSeat(self):
        # print("selSeat")
        
        try :
            driver.switch_to.frame(driver.find_element(By.XPATH, "//*[@id='ifrmSeatDetail']"))
            time.sleep(0.5)
            seats = driver.find_elements(By.XPATH, "//*[@id='TmgsTable']/tbody/tr/td/img[contains(@title, '" + g_floor + "') and contains(@title, '" + g_seatGrade + "') and contains(@title, '" + g_block + "')]")

            # for item in seats:
            #     # print(item.get_attribute("title"))

            if g_block != "" :
                seats.sort(key=lambda e: int(e.get_attribute("title")[e.get_attribute("title").find("열-")+2:]) )
            else :
                seats.sort(key=lambda e: ( e.get_attribute("title")[e.get_attribute("title").find("층-")+2:e.get_attribute("title").find("층-")+3] , int(e.get_attribute("title")[e.get_attribute("title").find("열-")+2:]) ))

            # print(seats)
            # print(len(seats))
            # print("------------------------------------------------------")

            # for item in seats:
            #     # print(item.get_attribute("title"))

            # if len(seats) < 1 :
            #     # print("원하는 좌석이 없으면 다음 회차 탐색")
            # else :

            global g_repeatCnt
            g_repeatCnt = 4 if len(seats) > 3 else len(seats)

            for i in range(0, g_repeatCnt) :
                seats[i].click()

            # global g_step
            # g_step = 3
            # self.macroManager()
            self.afterProcess()

        
        except:
            traceback.print_exc()

    # 좌석단계 좌석 재선택
    def reSelSeatSeat(self):
        # print("reSelSeat")
        try :
            driver.switch_to.default_content()
            driver.switch_to.frame(driver.find_element(By.XPATH, "//div[@id='divBookSeat']/iframe[@id='ifrmSeat']"))
            driver.find_element(By.XPATH, "/html/body/form[1]/div/div[1]/div[3]/div/div[4]/p[2]/a/img").click()
            self.selSeat()
        except:
            traceback.print_exc()

    # 결제단계 좌석 재선택
    def reSelSeatPay(self):
        # print("reSelSeat")
        try :
            driver.execute_script("fnPrevStep();")
            time.sleep(0.5)
            driver.switch_to.default_content()
            driver.switch_to.frame(driver.find_element(By.XPATH, "//div[@id='divBookSeat']/iframe[@id='ifrmSeat']"))
            self.selSeat()
        except:
            traceback.print_exc()

    # 좌석선택완료
    def completeSelSeat(self):
        
        driver.switch_to.default_content()
        driver.switch_to.frame(driver.find_element(By.XPATH, "//*[@id='ifrmBookStep']"))
        time.sleep(0.5)
        global g_repeatCnt
        g_repeatCnt = Select(driver.find_element(By.XPATH, "//*[contains(@id,'PriceRow00')]/td[3]/select")).getOptions().size()
        print(driver.find_element(By.XPATH, "//*[contains(@id,'PriceRow00')]/td[3]/select"))
        print("completeSelSeat :::" + str(g_repeatCnt))
        self.afterProcess()

    # 좌석선택 후 결제완료까지
    def afterProcess(self):
        # print("afterProcess")
        
        try :
            # 좌석선택완료 버튼
            driver.switch_to.default_content()
            driver.switch_to.frame(driver.find_element(By.XPATH, "//div[@id='divBookSeat']/iframe[@id='ifrmSeat']"))
            driver.find_element(By.XPATH, "/html/body/form[1]/div/div[1]/div[3]/div/div[4]/a").click()

            # 매수선택
            driver.switch_to.default_content()
            driver.switch_to.frame(driver.find_element(By.XPATH, "//*[@id='ifrmBookStep']"))
            # driver.implicitly_wait(g_wait)
            time.sleep(0.5)
            print(str(g_repeatCnt))
            ticketCntSel = Select(driver.find_element(By.XPATH, "//*[@id='PriceRow00" + str(g_repeatCnt) + "']/td[3]/select"))
            ticketCntSel.select_by_value(ticketCntSel.options.size())

            driver.switch_to.default_content()
            driver.find_element(By.XPATH, "//*[@id='SmallNextBtnImage']").click()

            # 생년월일
            driver.switch_to.default_content()
            driver.switch_to.frame(driver.find_element(By.XPATH, "//*[@id='ifrmBookStep']"))
            time.sleep(0.5)
            driver.find_element(By.XPATH, "//*[@id='YYMMDD']").send_keys(g_birth)
            driver.switch_to.default_content()
            driver.find_element(By.XPATH, "//*[@id='SmallNextBtnImage']").click()

            # 결제정보
            driver.switch_to.default_content()
            driver.switch_to.frame(driver.find_element(By.XPATH, "//*[@id='ifrmBookStep']"))
            driver.find_element(By.XPATH, "//*[@id='Payment_22004']/td/input").click() # 무통장입금
            Select(driver.find_element(By.XPATH, "//*[@id='BankCode']")).select_by_value("38056") # 신한은행
            driver.switch_to.default_content()
            driver.find_element(By.XPATH, "//*[@id='SmallNextBtnImage']").click()

            # 동의
            driver.switch_to.default_content()
            driver.switch_to.frame(driver.find_element(By.XPATH, "//*[@id='ifrmBookStep']"))
            time.sleep(0.5)
            driver.find_element(By.XPATH, "//*[@id='checkAll']").click()
            driver.switch_to.default_content()
            # driver.find_element(By.XPATH, "//*[@id='LargeNextBtnImage']").click()
        
        except:
            traceback.print_exc()


    def changeInputId(self):
        global g_id
        g_id = self.lineEditId.text()
    def changeInputPw(self):
        global g_pwd
        g_pwd = self.lineEditPw.text()
    def changeInputBirth(self):
        global g_birth
        g_birth = self.lineEditBirth.text()
    def changeInputNo(self):
        global g_goodsNum
        g_goodsNum = self.lineEditNo.text()
    def changeComboDate(self):
        global g_date
        g_date = self.cbDate.currentText()
    def changeComboHoicha(self):
        global g_hoicha
        g_hoicha = self.cbHoicha.currentText()
    def changeComboFloor(self):
        global g_floor
        g_floor = self.cbFoor.currentText()
    def changeComboGrade(self):
        global g_seatGrade
        g_seatGrade = self.cbGrade.currentText()
    def changeComboBlock(self):
        global g_block
        g_block = self.cbBlock.currentText()

    # # 매크로 매니저
    # def macroManager(self):
    #     # print("macroManager ::: " + str(g_step))
    #     # 예매하기
    #     if g_step == 0 :
    #         self.startInterpark()
    #     # 회차선택
    #     elif g_step == 1 :
    #         self.selDayHoicha()
    #     # 좌석선택
    #     elif g_step == 2 :
    #         self.selSeat()
    #     # 나머지 프로세스
    #     elif g_step == 3 :
    #         self.afterProcess()
    
    #def easyocrChar(self):
        # print("easyocrChar")
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

    # # 멜론티켓
    # def startMelon(self):
    #     driver = webdriver.Chrome('C:\chromedriver.exe')
    #     # 사이즈조절
    #     driver.set_window_size(1400, 1000)  # (가로, 세로)
    #     driver.get('https://ticket.interpark.com/Gate/TPLogin.asp') # 페이지 이동

    # # YES24
    # def startYes24(self):
    #     driver = webdriver.Chrome('C:\chromedriver.exe')
    #     # 사이즈조절
    #     driver.set_window_size(1400, 1000)  # (가로, 세로)
    #     driver.get('https://ticket.interpark.com/Gate/TPLogin.asp') # 페이지 이동

    # # 세종
    # def startSejong(self):
    #     driver = webdriver.Chrome('C:\chromedriver.exe')
    #     # 사이즈조절
    #     driver.set_window_size(1400, 1000)  # (가로, 세로)
    #     driver.get('https://ticket.interpark.com/Gate/TPLogin.asp') # 페이지 이동

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())