import requests, lxml.html
from bs4 import BeautifulSoup
import time

url = "https://login.xiami.com/member/login??spm=0.0.0.0.ApbFK8"
url2 = "http://www.xiami.com/artist/top/id/23282"

headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Mobile Safari/537.36"}

params = {"account": "18011370873", "pw": "Test_123"}

session = requests.Session()

#req2 = session.get(url, headers=headers)
#cookie = req2.cookies
#print(req2.cookies.get_dict())
#time.sleep(5)


req2 = session.get(url, headers=headers)
time.sleep(3)
login_html = lxml.html.fromstring(req2.text)
#print(login_html)
hidden_inputs = login_html.xpath(r'//form//input[@type="hidden"]')
form = {x.attrib["name"]: x.attrib["value"] for x in hidden_inputs}


form['account'] = "18011370873"
form['pw']= "Test_123"

print(form)

res = session.post(url, data=form)
time.sleep(5)

print(res.status_code)


#soup = BeautifulSoup(req.text, "lxml")
#print(soup.find("p"))

print(res.url)
print(res.cookies.get_dict())
