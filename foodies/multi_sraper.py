#temporary code
#!/usr/bin/env python3

#for scraping multiple page menus: chipotle, kerbey lane
import requests

from bs4 import BeautifulSoup

restaurant_url1 = 'https://www.yelp.com/menu/chipotle-mexican-grill-austin-14/'
restaurant_url2 =
restaurant_urls = [restaurant_url1, restaurant_url2]
for url in restaurant_urls:
    menu_sections = ["bowls", "burritos", "tacos", "salads"] # make this programatic
    
    for section in menu_sections:
        r = requests.get(url + section)
    
        soup = BeautifulSoup(r.content, 'html.parser')
        #print(soup.prettify())
        
        list_children = list(soup.children)
        #print(list_children)
        
        first = soup.find_all('h4')[0].get_text()
        #print(first)
        
        soup_list = soup.find_all('h4')
        a = []
        for x in soup_list:
            #print(x.get_text().strip())
            a.append(x.get_text().strip())
        
        print (a)
     


   
    
    
