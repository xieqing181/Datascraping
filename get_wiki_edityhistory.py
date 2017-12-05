from urllib.request import urlopen
from bs4 import BeautifulSoup

def getTitle(soup):
    title = soup.find("h1").get_text()
    #print(title)
    return title
    
def getHistoryIPs(title):
    html = urlopen("https://en.wikipedia.org/w/index.php?title="+title+"&action=history")
    soup = BeautifulSoup(html, "lxml")
    HistoryIPs = set()
    for link in soup.findAll("a", href=re.compile("^(/wiki/Special:Contributions/)\d*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in HistoryIPs:
                editor_IP = link.attrs['href']
                print("The editor IP is: "+str(editor_IP))
                HistoryIPs.add(editor_IP)
    return HistoryIPs
                

html = urlopen("https://en.wikipedia.org/wiki/Python_(programming_language)")
soup = BeautifulSoup(html, "lxml")

title = getTitle(soup)

#print(title)

getHistoryIPs(title)
