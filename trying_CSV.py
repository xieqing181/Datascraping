# -*- coding: utf-8 -*-
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://en.wikipedia.org/wiki/Comparison_of_text_editors")
soup = BeautifulSoup(html, "lxml")

csvFile = open("editor.csv", "wt", newline="", encoding='utf-8')

table = soup.find("table", {"class": "wikitable"})

#print(table)


rows = table.findAll("tr")

try:
    writer = csv.writer(csvFile)
    for row in rows:
        csvRow = []
        cells = row.findAll(["th","td"])
        for cell in cells:
            csvRow.append(cell.get_text())
            
        writer.writerow(csvRow)
finally:
    csvFile.close()

