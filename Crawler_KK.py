import requests
import pickle
import json


def cleans_dictionary(raw_dictionary):

    topics = raw_dictionary['topic_list']['topics']
    list_of_topics = []
    for i in topics:
        list_of_topics.append([i['id'], i['slug']])
    return list_of_topics


page_amount = 1
i = 1
new_submissions = []
crawler_condition = True
while i < 45:
    url = "https://community.gemsofwar.com/latest.json?no_definitions=true&page="+str(i)
    r = (requests.get(url)).text
    raw_dictionary = json.loads(r)
    if len(raw_dictionary['topic_list']['topics']) <= 0:
        crawler_condition = False
        break
    else:
        clean_dictionary = cleans_dictionary(raw_dictionary)
        new_submissions.extend(clean_dictionary)
        i += 1

with open("topic.karan.pickle", "wb") as output_file:
    pickle.dump(new_submissions, output_file)
