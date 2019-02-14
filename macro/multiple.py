from selenium import webdriver
from time import sleep


chrome_PATH = 'chromedriver_win32\chromedriver.exe'  # 크롬드라이버 경로
# driver1 = webdriver.Chrome(chrome_PATH)
# driver2 = webdriver.Chrome(chrome_PATH)
# driver3 = webdriver.Chrome(chrome_PATH)
# driver4 = webdriver.Chrome(chrome_PATH)
# driver1.get('https://www.yes24.com/Templates/FTLogin.aspx')  # 드라이버 오픈
# driver2.get('https://www.yes24.com/Templates/FTLogin.aspx')
# driver3.get('https://www.yes24.com/Templates/FTLogin.aspx')
# driver4.get('https://www.yes24.com/Templates/FTLogin.aspx')

win = 1
saveID = 'gustcool2'
savePWD = 'Vhql908034#$'
addr = 'http://ticket.yes24.com/Pages/Perf/Detail/DetailSpecial.aspx?IdPerf=32182'

for i in range(win):
    globals()['driver{}'.format(i)] = webdriver.Chrome(chrome_PATH)
    globals()['driver{}'.format(i)].get('https://www.yes24.com/Templates/FTLogin.aspx')  # 드라이버 오픈
    globals()['driver{}'.format(i)].implicitly_wait(3)  # 3초 기다림

    # 로그인
    globals()['driver{}'.format(i)].find_element_by_name('SMemberID').send_keys(saveID)
    sleep(0.5)
    globals()['driver{}'.format(i)].find_element_by_name('SMemberPassword').send_keys(savePWD)
    sleep(0.5)
    globals()['driver{}'.format(i)].find_element_by_id('btnLogin').click()

    globals()['driver{}'.format(i)].get(addr)

    a = globals()['driver{}'.format(i)].find_element_by_class_name('reserve')
    print(a)