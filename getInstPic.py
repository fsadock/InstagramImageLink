from lxml import html
import urllib.request
import requests
import os, platform

#url = input("\n\nInsert the instagram URL: ")
url = "https://www.instagram.com/p/BOngHOGDD28Dmrt0tevugnY1w779VaRprwMvDI0/"

pagina = requests.get(url)
content = html.fromstring(pagina.text)

pic = content.xpath('//meta[@property="og:image"]/@content')
pic = pic[0]
#print(pic)

if platform.system() == 'Windows':
	urllib.request.urlretrieve(pic, os.path.join(os.environ["HOMEPATH"], "Desktop\\foto.jpg"))
if platform.system() == 'Mac':
	urllib.request.urlretrieve(pic, os.path.join(os.path.expanduser('~'), 'Desktop'))

os.startfile(pic)

print("\n\nFOTO SALVA NA AREA DE TRABALHO!!!")