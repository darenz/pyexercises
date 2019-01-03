from bs4 import BeautifulSoup as BS
import requests
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

my_headers = {
        'Accept': 'text/html, application/xhtml+xml, application/xml;q=0.9, image/webp, */*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN, zh;q=0.8',
        'Upgrade-Insecure-Requests': '1',
        'Host': 'dict.youdao.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) \
                Chrome/48.0.2564.116 Safari/537.36'
    }

url2 = "http://free-ss.tk"
#html = requests.get(url2,my_headers)
#soup = BS(html.text,'html.parser')
#tables = soup.find_all('table')
#for each in tables:
#    print(each.text)

chrome_options = Options()
chrome_options.add_argument('User-Agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) \
                Chrome/48.0.2564.116 Safari/537.36')
chrome_options.add_argument('--disable-gpu')

#driver = webdriver.Chrome(chrome_options=chrome_options)
driver = webdriver.Chrome(executable_path='/bin/chromedriver',chrome_options=chrome_options)
#driver.get("http://www.baidu.com")
driver.get(url2)
data = driver.find_element_by_tag_name('body').text
print(data)

#table = soup.find('table',class_='compact stripe hover nowrap dataTable no-footer')
#ls = table.find_all('tr')

##for each in data:
##    table = each.find_all('td')
##    for e in table:
##        print(table.text)

#body = table.find_all('tr')
#print(len(body))
#print(body[0].text)
#
#ip_list = [] 
#if table:
#    ip_list = table.find_all('tr') 
#    print(len(ip_list))



