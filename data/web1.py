#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.yelp.com/menu/chipotle-mexican-grill-austin-14/bowls')

soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())

list_children = list(soup.children)
#print(list_children)

first = soup.find_all('h4')[0].get_text()
#print(first)

soup_list = soup.find_all('h4')

for x in soup_list:
    print(x.get_text().strip())


