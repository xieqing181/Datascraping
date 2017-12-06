from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO
from bs4 import BeautifulSoup

wordFile = urlopen("http://pythonscraping.com/pages/AWordDocument.docx").read()
wordFile = BytesIO(wordFile)
document = ZipFile(wordFile)
#print(document2)
xml_content = document.read('word/document.xml')
soup = BeautifulSoup(xml_content.decode('utf-8'))
#print(soup.prettify())
print(soup.findAll("w:t"))
for text in soup.findAll("w:t"):
    print(text.text)
