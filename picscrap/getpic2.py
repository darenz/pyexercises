#coding:utf-8
import  requests
import json
"""
Set-Cookie: ugid=ce08701842a7d46160190110ccd21c785161322;domain=.unsplash.com;path=/;expires=Sat, 25 Jan 2020 06:37:21 GMT
"""
"""
https://unsplash.com/napi/photos?page={}&per_page=12
""";
def reqHTML(url):
    headers={'Set-Cookie':'ugid=ce08701842a7d46160190110ccd21c785161322'}
    try:
        html = requests.get(url,verify=False,headers=headers)
        return html
    except:
        exit(-1)

def getIDs(page) :
    url = 'https://unsplash.com/napi/photos?page={}&per_page=12'.format(page)
    txt = reqHTML(url)
    js = json.loads(txt.text)
    li = []
    for each in js:
       #print(each['id'])
        li.append(each['id'])
    return li

def download(id):
    downURL = 'https://unsplash.com/photos/xxx/download'.replace('xxx',id)
    h = reqHTML(downURL)
    f = open("pictures/test"+id+".jpg","ab+")
    for chunk in h.iter_content(chunk_size=1024):
        if chunk:
            f.write(chunk)
            f.flush()

def main():
    for i in range(6,7):
        ids = getIDs(i)
        for j in range(len(ids)):
            download(ids[j])
            print("第%d页第%d张下载完成"%(i,j))

if __name__ == '__main__':
    main()
