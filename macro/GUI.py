import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from selenium import webdriver
from time import sleep


form_class = uic.loadUiType("main_window.ui")[0]
form_class_2 = uic.loadUiType("unopened_window.ui")[0]

class Second(QMainWindow, form_class_2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.checkBox.stateChanged.connect(self.onStateChange)
        self.checkBox_2.stateChanged.connect(self.onStateChange)

        self.pushButton.clicked.connect(self.reserve)


    def onStateChange(self, state):
        if state == Qt.Checked:
            if self.sender() == self.checkBox:
                self.checkBox_2.setChecked(False)
            else:
                self.checkBox.setChecked(False)


    def reserve(self):
        for i in range(myWindow.win):
            globals()['a{}'.format(i)] = globals()['driver{}'.format(i)].find_element_by_xpath('//*[@id="divSale"]/a[3]').text


        if self.checkBox.isChecked():
            for i in range(myWindow.win):
                a = globals()['driver{}'.format(i)].find_element_by_xpath('//*[@id="divSale"]/a[3]')
                b = a.text
                while True:
                    if b:
                        globals()['driver{}'.format(i)].implicitly_wait(3)
                        a = globals()['driver{}'.format(i)].find_element_by_xpath('//*[@id="divSale"]/a[3]')
                        b = a.text
                        print(b)
                    else:
                        a.click()
                        break


        elif self.checkBox_2.isChecked():
            while True:
                b = 0
                for i in range(myWindow.win):
                    if globals()['a{}'.format(i)]:
                        print(globals()['a{}'.format(i)])
                        globals()['driver{}'.format(i)].refresh()
                        globals()['a{}'.format(i)] = globals()['driver{}'.format(i)].find_element_by_xpath('//*[@id="divSale"]/a[3]').text
                        b = str(b) + globals()['a{}'.format(i)]
                print(b)
                if b == 0:
                    break

            for i in range(myWindow.win):
                globals()['driver{}'.format(i)].find_element_by_xpath('//*[@id="divSale"]/a[3]').click()



class MyWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.lineEdit.clicked.connect(self.lineEdit.clear)
        self.lineEdit_2.clicked.connect(self.lineEdit_2.clear)
        self.lineEdit_3.clicked.connect(self.lineEdit_3.clear)

        self.pushButton.clicked.connect(self.login)

        self.checkBox.stateChanged.connect(self.onStateChange)
        self.checkBox_2.stateChanged.connect(self.onStateChange)


        self.second = Second()
        self.pushButton_2.clicked.connect(self.reserve)



    def login(self):
        saveID = self.lineEdit.text()
        savePWD = self.lineEdit_2.text()
        addr = self.lineEdit_3.text()
        win = self.spinBox.text()
        self.win = int(win)
        chrome_PATH = 'chromedriver_win32\chromedriver.exe'  # 크롬드라이버 경로

        for i in range(self.win):

            globals()['driver{}'.format(i)] = webdriver.Chrome(chrome_PATH)
            globals()['driver{}'.format(i)].get('https://www.yes24.com/Templates/FTLogin.aspx') # 드라이버 오픈
            globals()['driver{}'.format(i)].implicitly_wait(3) # 3초 기다림

            #로그인
            globals()['driver{}'.format(i)].find_element_by_name('SMemberID').send_keys(saveID)
            sleep(0.5)
            globals()['driver{}'.format(i)].find_element_by_name('SMemberPassword').send_keys(savePWD)
            sleep(0.5)
            globals()['driver{}'.format(i)].find_element_by_id('btnLogin').click()

            globals()['driver{}'.format(i)].get(addr)



# 크롤링 필요, 예매하기 버튼 클릭해서 원하는 xpath가 있으면 클릭하고 아니면 계속 리프레시
# 그리고 다중창 어떤식으로 처리할수 있는지 찾아봐야됨
    def reserve(self):
        # for i in range(self.win):
        #     globals()['driver{}'.format(i)].find_element_by_xpath('//*[@id="divSale"]/a[3]').click()
        if self.checkBox.isChecked():
            for i in range(self.win):
                globals()['driver{}'.format(i)].find_element_by_xpath('//*[@id="divSale"]/a[3]').click()

        elif self.checkBox_2.isChecked():
            self.second.show()


    def onStateChange(self, state):
        if state == Qt.Checked:
            if self.sender() == self.checkBox:
                self.checkBox_2.setChecked(False)
            else:
                self.checkBox.setChecked(False)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()


