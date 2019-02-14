import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from selenium import webdriver
import selenium
from time import sleep
import threading


form_class = uic.loadUiType("main_window.ui")[0]
form_class_2 = uic.loadUiType("unopened_window.ui")[0]

class Second(QMainWindow, form_class_2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.checkBox.stateChanged.connect(self.onStateChange)
        self.checkBox_2.stateChanged.connect(self.onStateChange)

        self.pushButton.clicked.connect(self.unopened)
        self.pushButton_2.clicked.connect(self.stop)

    stop_confirm = 0

    def onStateChange(self, state):
        if state == Qt.Checked:
            if self.sender() == self.checkBox:
                self.checkBox_2.setChecked(False)
            else:
                self.checkBox.setChecked(False)


    def auto_refresh(self, driver):

        while True:
            try:
                driver.implicitly_wait(3)
                division = driver.find_element_by_xpath('//*[@id="divSale"]/a[3]').text
                if division:
                    driver.get(myWindow.addr)
                    if self.stop_confirm:
                        self.stop_confirm = 0
                        break
                else:
                    driver.find_element_by_xpath('//*[@id="divSale"]/a[3]').click()
                    break

            except selenium.common.exceptions.NoSuchElementException:
                driver.get(myWindow.addr)


    def manual_refresh(self, driver):

        while True:
            try:
                driver.implicitly_wait(3)
                division = driver.find_element_by_xpath('//*[@id="divSale"]/a[3]').text
                if division:
                    print(division)
                    if self.stop_confirm:
                        self.stop_confirm = 0
                        break
                else:
                    driver.find_element_by_xpath('//*[@id="divSale"]/a[3]').click()
                    break

            except selenium.common.exceptions.NoSuchElementException:
                driver.get(myWindow.addr)


    def unopened(self):
        if self.checkBox.isChecked():
            for i in range(myWindow.win):
                threading.Thread(target=self.manual_refresh, args=(myWindow.a[i],)).start()
                sleep(1)

        elif self.checkBox_2.isChecked():
            for i in range(myWindow.win):
                threading.Thread(target=self.auto_refresh, args=(myWindow.a[i],)).start()
                sleep(1)

    def stop(self):
        self.stop_confirm = 1
        msgbox = QMessageBox(self)
        msgbox.about(self, 'Stop', 'Stop Button is Pushed')



class MyWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.lineEdit.clicked.connect(self.lineEdit.clear)
        self.lineEdit_2.clicked.connect(self.lineEdit_2.clear)
        self.lineEdit_3.clicked.connect(self.lineEdit_3.clear)

        self.checkBox.stateChanged.connect(self.onStateChange)
        self.checkBox_2.stateChanged.connect(self.onStateChange)

        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(self.reserve)

        self.second = Second()

    a = []

    def login_thread(self, driver, saveID, savePWD, addr, i):

        chrome_PATH = 'chromedriver_win32\chromedriver.exe'
        driver = webdriver.Chrome(chrome_PATH)
        self.a.insert(i, driver)
        driver.get('https://www.yes24.com/Templates/FTLogin.aspx')
        driver.implicitly_wait(3)
        driver.find_element_by_name('SMemberID').send_keys(saveID)
        sleep(0.5)
        driver.find_element_by_name('SMemberPassword').send_keys(savePWD)
        sleep(0.5)
        driver.find_element_by_id('btnLogin').click()
        driver.get(addr)
        driver.implicitly_wait(3)



    def login(self):
        self.addr = self.lineEdit.text()
        saveID = self.lineEdit_2.text()
        savePWD = self.lineEdit_3.text()
        win = self.spinBox.text()
        self.win = int(win)
        for i in range(self.win):
            threading.Thread(target=self.login_thread, args=('driver{}'.format(i), saveID, savePWD, self.addr, i)).start()
            sleep(1)

    def reserve_thread(self, driver):
        try:
            driver.find_element_by_xpath('//*[@id="divSale"]/a[3]').click()
            driver.switch_to.window(driver.window_handles[1])
            self.last_reserve(driver)
        except selenium.common.exceptions.NoSuchElementException:
            driver.switch_to.window(driver.window_handles[0])
            driver.get(self.addr)
            driver.implicitly_wait(3)
            self.reserve_thread(driver)
        except selenium.common.exceptions.NoSuchWindowException:
            driver.switch_to.window(driver.window_handles[0])
            driver.find_element_by_xpath('//*[@id="divSale"]/a[3]').click()
            driver.switch_to.window(driver.window_handles[1])

    def last_reserve(self, driver):
        try:
            driver.find_element_by_xpath(self.date3).click()
            driver.find_element_by_xpath('//*[@id="ulTime"]/li').click()
            driver.find_element_by_xpath('//*[@id="btnSeatSelect"]').click()
        except selenium.common.exceptions.NoSuchElementException:
            driver.find_element_by_xpath('//*[@id="ulTime"]/li').click()
            driver.find_element_by_xpath('//*[@id="btnSeatSelect"]').click()

    def reserve(self):
        if not self.a:
            msgbox = QMessageBox(self)
            msgbox.about(self, 'Error', 'Please Push Login Button First!!!')
        else:
            self.date = self.calendarWidget.selectedDate()
            self.date2 = self.date.toString('yyyy-MM-dd')
            self.date3 = '//*[@id="' + self.date2 + '"]'
            if self.checkBox.isChecked():
                for i in range(self.win):
                    threading.Thread(target=self.reserve_thread, args=(self.a[i],)).start()
                    sleep(1)

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


