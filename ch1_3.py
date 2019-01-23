import urllib.request as req

url = "http://gw.tbroad.com/"
res = req.urlopen(url)
# data = res.read()
# text = data.decode("utf-8")
# print(text)
# print("################")

#data1 = res.geturl()
#print('geturl: {0}'.format(data1))
#print("################")

data2 = res.info()
print('info: {0}'.format(data2))
print("################")


#data3 = res.getcode()
#print('getcode: {0}'.format(data3))
#print("################")
