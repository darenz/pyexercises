import requests_html

session = requests_html.HTMLSession()

import pymysql

db = pymysql.connect("localhost","root","z9988321","testbase")
cursor = db.cursor()
testTitle = "this is a title"
testURL = "http://example/test/url"
cursor.execute("insert into picfetch(PicTitle,URL) values ('{}','{}')".format(testTitle,testURL))
cursor.execute("desc picfetch")
cursor.execute("select * from picfetch")
result = cursor.fetchall()

print(result)

