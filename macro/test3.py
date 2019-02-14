import threading
from selenium import webdriver
from time import sleep

win = 3

chrome_PATH = 'chromedriver_win32\chromedriver.exe'

a = []

def driver_get(driver):
    saveID = 'gustcool2'
    savePWD = 'Vhql908034#$'
    addr = 'http://ticket.yes24.com/Pages/Perf/Detail/Detail.aspx?IdPerf=32206&Gcode=009_109'
    chrome_PATH = 'chromedriver_win32\chromedriver.exe'
    driver = webdriver.Chrome(chrome_PATH)
    driver.get('https://www.yes24.com/Templates/FTLogin.aspx')
    driver.implicitly_wait(3)
    driver.find_element_by_name('SMemberID').send_keys(saveID)
    sleep(0.5)
    driver.find_element_by_name('SMemberPassword').send_keys(savePWD)
    sleep(0.5)
    driver.find_element_by_id('btnLogin').click()
    driver.get(addr)
    a.append(driver)

for i in range(win):
    threading.Thread(target=driver_get, args = ('driver{}'.format(i),)).start()



