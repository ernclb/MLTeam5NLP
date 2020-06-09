import requests
import json
import pprint
import pickle

def cleans_dictionary(raw_dictionary):
    #get all the slugs and topic_id's out of this dictionary (make sure the parameters are string)
    #and make a new dictionary with the 30 topics just the id's and slugs
    #new_submissions = [{'topic_id': 23124,'slug':'debit-cards'},{'topic_id': 846283,'slug':'credit-card'}]
    topics = raw_dictionary['topic_list']['topics']
    list_of_topics = []
    for i in topics:
        list_of_topics.append([i['id'],i['slug']])
    return list_of_topics


page_amount = 7
i = 1
new_submissions = []
crawler_condition = True
while crawler_condition == True:
    url = "https://community.bnz.co.nz/latest.json?no_definitions=true&page="+str(i)
    r = (requests.get(url)).text
    raw_dictionary = json.loads(r)
    if len(raw_dictionary['topic_list']['topics']) <= 0:
        crawler_condition = False
        break
    else:
        clean_dictionary = cleans_dictionary(raw_dictionary)
        new_submissions.extend(clean_dictionary)
        i += 1

with open("all_the_topic_names.pickle", "wb") as output_file:
     pickle.dump(new_submissions, output_file)
