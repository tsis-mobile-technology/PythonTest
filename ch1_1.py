import urllib.request as req

url = "http://uta.pw/shodou/img/28/214.png"
savename = "test.png"

req.urlretrieve(url, savename)
print("saving ok")
