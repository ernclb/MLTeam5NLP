import requests
print('hello')
r = requests.get('http://google.com')
print(r.text)
print(help(r))
#Test addition