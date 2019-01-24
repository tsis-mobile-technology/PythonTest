
from bs4 import BeautifulSoup
import urllib.request as req
import sys

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
