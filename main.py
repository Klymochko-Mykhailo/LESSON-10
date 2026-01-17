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



# Завдання 3

import requests

response = requests.get("http://books.toscrape.com/")
text = response.text

titles = []
prices = []

for elem in text.split('title="'):
    if '"' in elem:
        titles.append(elem.split('"')[0])

for elem in text.split('£'):
    if elem[:1].isdigit():
        prices.append("£" + elem[:5])

for i in range(len(prices)):
    print(f"Книга: {titles[i]} | Ціна: {prices[i]}")
