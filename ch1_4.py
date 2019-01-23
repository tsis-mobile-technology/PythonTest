import urllib.request as req
import urllib.parse

API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

values = {
	'stnId': '108'
}

param = urllib.parse.urlencode(values)

url = API + "?" + param
print("url=", url)

data = req.urlopen(url).read()
text = data.decode("utf-8")
print(text)
