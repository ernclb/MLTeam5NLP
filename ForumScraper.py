import requests
import pprint
import json
page_val = str(input('What page would you like to print: '))
url = "https://community.bnz.co.nz/latest.json?no_definitions=true&page="+page_val
r = requests.get(url)
dic = json.loads(r.text)
pprint.pprint(dic)