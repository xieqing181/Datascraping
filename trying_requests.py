import requests

params = {'firstname': 'xie', 'lastname': 'qing'}
r = requests.post("http://pythonscraping.com/pages/files/processing.php", data=params)
print(r.text)
