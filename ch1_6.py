from bs4 import BeautifulSoup
import urllib.request as req

#url = "http://gw.tbroad.com/"
url = "http://m.exchange.daum.net/mobile/exchange/exchangeMain.daum"
res = req.urlopen(url)
data = res.read()
text = data.decode("utf-8")
#print(text)

html = text

soup = BeautifulSoup(html, 'html.parser')

title = soup.html.head.title
print("title=" + title.string)

img = soup.find_all("img")
for img_src in img:
	print("img=" + img_src.get("src"))

#input = soup.find_all("input")
#for input_src in input:
#	print("input.type=" + input_src.get("type") + ", input.id=" + input_src.get("id"))

#link = soup.find_all("link")
#for link_src in link:
#	print("link.type=" + link_src.get("type") + ", link.href=" + link_src.get("href"))


tag = soup.div
print(tag)

