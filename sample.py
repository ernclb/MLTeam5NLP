import requests
import pprint
import json

url = "https://community.bnz.co.nz/latest.json?no_definitions=true&page="+str(1)
r = (requests.get(url)).text
raw_dictionary = json.loads(r)
print("First Dic:",raw_dictionary["topic_list"]["topics"])
# print("Raw dictionary:",raw_dictionary)
