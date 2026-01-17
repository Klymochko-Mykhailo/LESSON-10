# Завдання 1

import requests

response = requests.get("http://books.toscrape.com/")
response_text = response.text

response_parse = response_text.split('title="')

for elem in response_parse:
    if elem.startswith("") and '"' in elem:
        book_title = elem.split('"')[0]
        print(book_title)



# Завдання 2

import requests

response = requests.get("http://books.toscrape.com/")
response_text = response.text

response_parse = response_text.split('£')

for elem in response_parse:
    if elem[:1].isdigit():
        price = "£" + elem[:5]
        print(price)



