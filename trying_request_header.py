import requests
from bs4 import BeautifulSoup

session = requests.Session()

html = "https://www.whatismybrowser.com/detect/what-http-headers-is-my-browser-sending"

headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", 
            "User-Agent": "Mozilla/5.x (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Mobile Safari/537.49"}

req = session.get(html, headers=headers)

soup = BeautifulSoup(req.text, "lxml")
print(soup.find("table", {"class": "table table-striped"}).text)
