from selenium import webdriver
from time import sleep

chrome_PATH = 'chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(chrome_PATH)
driver.get('https://www.yes24.com/Templates/FTLogin.aspx')
driver.implicitly_wait(10)
driver.find_element_by_name('SMemberID').send_keys('gustcool2')
sleep(0.5)
driver.find_element_by_name('SMemberPassword').send_keys('Vhql908034#$')
sleep(0.5)
driver.find_element_by_id('btnLogin').click()
driver.get('http://ticket.yes24.com/Pages/Perf/Detail/DetailSpecial.aspx?IdPerf=32203')
driver.implicitly_wait(10)
driver.find_element_by_xpath('//*[@id="divSale"]/a[3]').click()
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)

driver.find_element_by_xpath('//*[@id="2019-04-06"]').click()



