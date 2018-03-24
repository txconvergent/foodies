#temporary code
#!/usr/bin/env python3
import requests

from bs4 import BeautifulSoup

restarurant_url = 'https://www.yelp.com/menu/chipotle-mexican-grill-austin-14/'

restaruant_urls = [url, url, url]
for url in restaurant_urls:
    menu_sections = ["bowls", "burritos", "tacos"] # make this programatic
    
    for section in menu_sections:
        r = requests.get(url + section)
    
        soup = BeautifulSoup(r.content, 'html.parser')
        #print(soup.prettify())
        
        list_children = list(soup.children)
        #print(list_children)
        
        first = soup.find_all('h4')[0].get_text()
        #print(first)
        
        soup_list = soup.find_all('h4')
        
        for x in soup_list:
            print(x.get_text().strip())
        
    
    
    
    
#f= open('menuitems.csv','wb')
#csv_writer= csv.writer(f)  
    
    
    
#import pandas as pd 
#df = pd.DataFrame(records,columns=['menu'])
    
#df.to_csv('menuitems.csv', index=False, encoding= 'utf-8')

#write data to csv file 
#import csv
#excel= csv.writer(open('menu-items.csv','w'))
#excel.writerow(['Item', 'Link'])
#excel.writerow([first ,links])


