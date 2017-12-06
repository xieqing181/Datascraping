from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open

def readPFD(pdfFile):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparms = LAParams()
    device = TextConverter(rsrcmgr, retstr,)
    
    process_pdf(rsrcmgr, device, pdfFile)
    device.close()
    
    content = retstr.getvalue()
    retstr.close()
    return content
    
pdfFile = urlopen("http://pythonscraping.com/pages/warandpeace/chapter1.pdf")
outputString = readPFD(pdfFile)
print(outputString)
pdfFile.close()
