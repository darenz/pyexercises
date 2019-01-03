from bs4 import BeautifulSoup
import urllib.request

url = "http://dict.youdao.com/w/"
my_headers = {
        'Accept': 'text/html, application/xhtml+xml, application/xml;q=0.9, image/webp, */*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN, zh;q=0.8',
        'Upgrade-Insecure-Requests': '1',
        'Host': 'dict.youdao.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) \
                       Chrome/48.0.2564.116 Safari/537.36'
    }


word = input("word:")
url += word;

#html = urllib.request.Request(url,headers=my_headers)
html = urllib.request.urlopen(url) 
data = html.read()
print(data)
soup = BeautifulSoup(data,'html.parser')
trans_container = soup.find('div',id='trans-container')
trans = trans_container.find_all('li')
print(trans)

