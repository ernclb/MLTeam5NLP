import requests
import pickle
from bs4 import BeautifulSoup


def get_forum_message(message):
    soup = BeautifulSoup(message, 'html.parser')
    # div = soup.find("div" "cooked")
    ht = soup.find_all("p")
    # print(ht)
    submission_text = ''
    for i in ht:
        submission_text += i.get_text()
    return submission_text


with open("topic.karan.pickle", "rb") as input_file:
    new_submissions = pickle.load(input_file)

dic = []
breaker = len(new_submissions)
for i in range(breaker):
    print((i/breaker)*100)
    submission = new_submissions[i]
    topic_url = ("https://community.gemsofwar.com/t/" + submission[1] + '/' + str(submission[0]))
# url = 'https://community.gemsofwar.com/'
# topic_url = "https://community.gemsofwar.com/t/gow-wiki-here/3496"
    response = requests.get(topic_url)
    message = response.text
# print(message)
    dic.append([topic_url, get_forum_message(message)])
# print(dic)
with open("text_submissions_karan.pickle", "wb") as output_file:
    pickle.dump(dic, output_file)
