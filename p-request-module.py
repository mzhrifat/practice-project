"""
import requests
x= requests.delete('https://w3school.com/python/demopage.php')
print(x.text)


import requests

url = 'https://w3schools.com/python/demopage.php'

#find a free proxy address and send your request via that proxy:
x = requests.delete(url, proxies = { "https" : "https://1.1.0.1:80"})

print(x.status_code)


import requests

x = requests.get('https://w3school.com',)

print(x.status_code)
"""

import requests
x=requests.head('https://www.w3schools.com/python/demopage.php')

print(x.headers)