import requests
import json
import pprint
import pickle
import time
from bs4 import BeautifulSoup

# this can also be done with scrapy where I only scrape a certain xpath. 
# To do that use: xpath = '/html/body/div/div[2]'

def get_forum_message(message):
    soup = BeautifulSoup(message,features="lxml")
    div = soup.find("div", {"itemprop": "articleBody"})
    ht = div.findAll('p')
    submission_text = ''
    for i in ht:
        submission_text += i.get_text() 
    return submission_text


with open("all_the_topic_names.pickle", "rb") as input_file:
    new_submissions = pickle.load(input_file)

dic = []
breaker = len(new_submissions)
for i in range(breaker):
    print((i/breaker)*100)
    submission = new_submissions[i]
    topic_url = ("https://community.bnz.co.nz/t/" + submission[1] + '/' + str(submission[0]))
    response = requests.get(topic_url)
    message = response.text
    dic.append([topic_url,get_forum_message(message)])

with open("text_submissions.pickle", "wb") as output_file:
    pickle.dump(dic, output_file)
