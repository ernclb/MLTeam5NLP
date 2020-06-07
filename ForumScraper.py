import requests
import pprint
import json
page_val = str(input('What page would you like to print: '))
url = "https://community.bnz.co.nz/latest.json?no_definitions=true&page="+page_val
r = (requests.get(url)).text
dic = json.loads(r)
with open('text.txt', 'w') as f:
    print(r, file=f)
pprint.pprint(dic)