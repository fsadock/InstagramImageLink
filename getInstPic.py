from lxml import html
import urllib.request
import requests
import os, platform

url = input("\n\nInsert the instagram URL: ")

page = requests.get(url)
content = html.fromstring(page.text)

#get the proper link
pic = content.xpath('//meta[@property="og:image"]/@content')
pic = pic[0]

if platform.system() == 'Windows':
	urllib.request.urlretrieve(pic, os.path.join(os.environ["HOMEPATH"], "Desktop\\foto.jpg"))
if platform.system() == 'Mac':
	urllib.request.urlretrieve(pic, os.path.join(os.path.expanduser('~'), 'Desktop'))

#opens the picture on the browser
os.startfile(pic)

print("\n\nSAVED ON DESKTOP!!!")
