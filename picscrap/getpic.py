import pymysql
import requests_html
import re

def getData(session,page,rec):
    try:
        html = session.get(r"http://www.doutula.com/photo/list/?page={}".format(page))
        text = html.text
        result = rec.findall(text)
    except:
        result = []
    return result

db = pymysql.connect("localhost","root","z9988321","testbase")
cursor = db.cursor()
session = requests_html.HTMLSession()
pattern = r'data-original="(.*?)".*?alt="(.*?)"'
rec = re.compile(pattern,re.S)
for page in range(50):
    result = getData(session,page,rec)
    if(len(result)==0):
        break;
    for url,title in result:
        print(url,title)
        cursor.execute("insert into picfetch(PicTitle,URL) values ('{}','{}')".format(title,url))
db.commit()
db.close()
