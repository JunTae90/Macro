from selenium import webdriver
import threading
from time import sleep




def manual_refresh(driver):
    chrome_PATH = 'chromedriver_win32\chromedriver.exe'
    driver = webdriver.Chrome(chrome_PATH)
    driver.get('http://ticket.yes24.com/Pages/Perf/Detail/Detail.aspx?IdPerf=32291')
    division = driver.find_element_by_xpath('//*[@id="divSale"]/a[3]').text
    while True:
        if division:
            division = driver.find_element_by_xpath('//*[@id="divSale"]/a[3]').text
            print(division)
            driver.implicitly_wait(3)
        else:
            driver.find_element_by_xpath('//*[@id="divSale"]/a[3]').click()
            sleep(10)
            break



threading.Thread(target=manual_refresh, args=('driver0',)).start()
