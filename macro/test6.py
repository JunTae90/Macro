import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from selenium import webdriver
from time import sleep
import threading


form_class = uic.loadUiType("main_window.ui")[0]
form_class_2 = uic.loadUiType("unopened_window.ui")[0]



class MyWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_2.clicked.connect(self.test)


    def test(self):
        date = self.calendarWidget.selectedDate()
        date2 = date.toString('yyyy-MM-dd')
        date3 = '//*[@id="'+date2+'"]'
        print(date3)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
