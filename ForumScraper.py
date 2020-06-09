import requests
import pprint
import json

page_amount = 7
i = 1
new_submissions = []


while 1:
    clean_dictionary_list=[]
    url = "https://community.bnz.co.nz/latest.json?no_definitions=true&page="+str(i)
    r = (requests.get(url)).text
    raw_dictionary = json.loads(r)
    raw_dictionary_topics = raw_dictionary["topic_list"]["topics"]
    if len(raw_dictionary_topics['topic_list']['topics']) == 0:
        break
      
    clean_dictionary_list = cleans_dictionary(raw_dictionary_topics)
    new_submissions += clean_dictionary_list

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
    list_dictionary =[]
    
    for dic in raw_dictionary:
        temp_dict=dict()
        temp_dict['topic_id'] = dic['topic_id']
        temp_dict['slug'] = dic['slug']
        list_dictionary.append(temp_dict)
    return list_dictionary    

