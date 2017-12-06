import csv
from urllib.request import urlopen
from io import StringIO

data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii', 'ignor')
dataFile = StringIO(data)
dictReader = csv.DictReader(dataFile)

print(dictReader.fieldnames)

for row in dictReader:
    print(row)
    

