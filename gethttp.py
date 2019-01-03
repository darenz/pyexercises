import urllib.request

#138.201.81.199

url = urllib.request.urlopen("https://129.42.60.212:80")
print(url.read())

