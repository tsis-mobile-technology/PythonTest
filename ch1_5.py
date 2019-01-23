import sys
import urllib.request
import urllib.parse

if len(sys.argv) <= 1:
	print("USAGE: ch5_src.py <regionNumber>")
	sys.exit()
regionNumber = sys.argv[1]

API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

values = {
	'stnId': regionNumber
}

param = urllib.parse.urlencode(values)

url = API + "?" + param
print("url=", url)

data = urllib.request.urlopen(url).read()
text = data.decode("utf-8")
print(text)
