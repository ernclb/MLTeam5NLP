import requests
import pprint
import json
from bs4 import BeautifulSoup
import urllib
import pickle

def cleans_dictionary(raw_dictionary):
 
    post_dist = {}
    global new_submissions
    for post in raw_dictionary['topic_list']['topics'] :
      
      post_dist['id'] = str(post['id'])
      post_dist['slug'] = str(post['slug'])
      new_submissions.append(post_dist)
      post_dist={}
    
def get_forum_message(page):    

    soup = BeautifulSoup(page.content, 'html.parser')
    for anchors in soup.find_all('a'): #To remove hyperlinks
      anchors.extract()

    postData = soup.find_all("p")
    
    posts = []
    for post in postData:
        posts.append(BeautifulSoup(str(post)).get_text().strip().replace("\t", ""))#removing tabs

    posts_stripped = [x.replace("\n","") for x in posts]#removing newlines

    return posts_stripped

page_amount = 7
new_submissions = []
clean_posts=[]
for page in range(1,page_amount+1) :
    url = "https://community.bnz.co.nz/latest.json?no_definitions=true&page="+str(page)
    r = (requests.get(url)).text
    raw_dictionary = json.loads(r)
    cleans_dictionary(raw_dictionary)
    

topic_url = "https://community.bnz.co.nz/t/"
for submission in new_submissions:
    topic_url += (submission['slug'] + '/' + submission['id'])
    page = requests.get(topic_url)
    clean_posts.append([topic_url,get_forum_message(page)])
    topic_url = "https://community.bnz.co.nz/t/"


with open("Data.pickle", "wb") as output_file:
    pickle.dump(clean_posts, output_file)
