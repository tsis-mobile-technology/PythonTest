
from bs4 import BeautifulSoup
import urllib.request as req
from urllib.parse import urljoin
import sys
import re

url = "https://ko.wikipedia.org/wiki/%EC%9C%A4%EB%8F%99%EC%A3%BC"
#res = urllib.urlopen(url)
# han crash
res = req.urlopen(url).read().decode(req.urlopen(url).headers.get_content_charset())
soup = BeautifulSoup(res, 'html.parser')

# #toc > ul > li.toclevel-1.tocsection-2
a_list = soup.select("#toc > ul > li span.toctext")
print(a_list)
#reload(sys)
#sys.setdefaultencoding('utf-8')
#print(sys.getdefaultencoding())

for a in a_list:
	name = a.string
	print("-", name)
#CSS 선택자로 추출하는 예제
sel =  lambda q : print("24>", soup.select_one(q).string)
sel("#mw-head #p-personal-label")

#정표현식과 조립하여 추출 예제
li = soup.find_all(href=re.compile(r"^http*://"))
for e in li:
	print("30>", e.attrs['href'])

#상대경로 처리 방법
aa = soup.select("a[href]")
for a in aa:
	#print("36>", a.attrs['href'] )
	bb = urljoin(url, a.attrs['href'])
	print("38>",bb)
