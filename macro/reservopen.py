from selenium import webdriver
from time import sleep


chrome_PATH = 'chromedriver_win32\chromedriver.exe'  # 크롬드라이버 경로

win = 1
saveID = 'gustcool2'
savePWD = 'Vhql908034#$'
addr = 'http://ticket.yes24.com/Pages/Perf/Detail/DetailSpecial.aspx?IdPerf=32307'
addr2 = 'http://ticket.yes24.com/Pages/Perf/Detail/DetailSpecial.aspx?IdPerf=32317'

driver = webdriver.Chrome(chrome_PATH)
driver.get('http://ticket.yes24.com/Pages/Perf/Detail/DetailSpecial.aspx?IdPerf=32317')  # 드라이버 오픈
driver.implicitly_wait(3)  # 3초 기다림




a = driver.find_element_by_xpath('//*[@id="divSale"]/a[3]')
b = a.text
while True:
    if b:
        driver.refresh()
    else:
        a.click()
        break
