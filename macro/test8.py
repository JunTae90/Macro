from selenium import webdriver
import threading

chrome_PATH = 'chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(chrome_PATH)

driver.get('https://www.yes24.com/Templates/FTLogin.aspx')
driver.find_element_by_name('SMemberID').send_keys('gustcool2')
driver.find_element_by_name('SMemberPassword').send_keys('Vhql908034#$')
driver.find_element_by_id('btnLogin').click()
driver.get('http://ticket.yes24.com/Pages/Perf/Detail/DetailSpecial.aspx?IdPerf=32372')
driver.find_element_by_xpath('//*[@id="divSale"]/a[3]').click()
driver.switch_to.window(driver.window_handles[1])
driver.implicitly_wait(3)
driver.find_element_by_xpath('//*[@id="2019-03-09"]').click()
driver.find_element_by_xpath('//*[@id="ulTime"]/li').click()
driver.find_element_by_xpath('//*[@id="btnSeatSelect"]').click()
iframe = driver.find_element_by_xpath('//*[@id="divFlash"]/iframe')
driver.implicitly_wait(3)
driver.switch_to.frame(iframe)
driver.implicitly_wait(3)


while True:
    a = driver.find_elements_by_css_selector(".s6, .s8, .s9, .s4, .s13")
    if a:
        for i in a:
            print(a.index(i))
        break




