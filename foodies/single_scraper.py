#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
     
#for scraping one page menus:madam mams, noon , kerbey

madam_mams = 'https://www.yelp.com/menu/madam-mams-austin-6'
noon = 'https://www.yelp.com/menu/noon-mediterranean-new-york-2'
kerbey1 = 'https://www.yelp.com/menu/kerbey-lane-cafe-austin-3/24-hour-menu'
kerbey2 = 'https://www.yelp.com/menu/kerbey-lane-cafe-austin-3/spring-menu'
kerbey3 = 'https://www.yelp.com/menu/kerbey-lane-cafe-austin-3/kids-menu'
kerbey4 = 'https://www.yelp.com/menu/kerbey-lane-cafe-austin-3/gluten-free-and-vegan'
qdoba = 'https://www.yelp.com/menu/qdoba-mexican-eats-austin'

restaurant_urls = [madam_mams, noon, kerbey1, kerbey2, kerbey3, kerbey4, qdoba]
    
for url in restaurant_urls:
        r = requests.get(url)
    
        soup = BeautifulSoup(r.content, 'html.parser')
        #print(soup.prettify())
        
        list_children = list(soup.children)
        #print(list_children)
        
        first = soup.find_all('h4')[0].get_text()
        #print(first)
        
        soup_list = soup.find_all('h4')
        
        single_list = []
        for x in soup_list:
            #print(x.get_text().strip())
            single_list.append(x.get_text().strip())
            
        print("MENU ITEMS:", single_list)