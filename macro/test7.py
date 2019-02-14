from selenium import webdriver
import selenium

chrome_PATH = 'chromedriver_win32\chromedriver.exe'

driver = webdriver.Chrome(chrome_PATH)
# try:
driver.find_element_by_xpath('//*[@id="divSale"]/a[3]').text
# except selenium.common.exceptions.NoSuchElementException:
#     driver.get('http://www.naver.com')