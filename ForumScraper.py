import requests
import pprint
import json

page_amount = 7
i = 1
new_submissions = []
while len(dic['topic_list']['topics']) > 0:
    url = "https://community.bnz.co.nz/latest.json?no_definitions=true&page="+i
    r = (requests.get(url)).text
    raw_dictionary = json.loads(r)
    clean_dictionary = cleans_dictionary(raw_dictionary)
    new_submissions.append(clean_dictionary)
    i += 1

topic_url = "https://community.bnz.co.nz/t/"
for submission in new_submissions:
    topic_url += (submission['slug'] + '/' + submission['topic_id'])
    message_in_html = requests.get(topic_url).text
    get_forum_message(message_in_html)

def get_forum_message(message):
    #Use the html to parse and get the message submission
    
def cleans_dictionary(raw_dictionary):
    #get all the slugs and topic_id's out of this dictionary (make sure the parameters are string)
    #and make a new dictionary with the 30 topics just the id's and slugs
    #new_submissions = [{'topic_id': 23124,'slug':'debit-cards'},{'topic_id': 846283,'slug':'credit-card'}]