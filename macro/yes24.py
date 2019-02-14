from bs4 import BeautifulSoup
import requests


url = 'http://ticket.yes24.com/Pages/Popup/Mainpopup.aspx'
source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text, 'lxml')
code_finda = soup.findAll('a')
print(code_finda)


for i in code_finda:
    if 'title' in i.attrs:
        finda_title = i.attrs['title']
        print(finda_title)
        # a_title = i.attrs['title']
        # b_link = i.attrs['ParentLink']
        # a.append(b)
        # print(a_title)