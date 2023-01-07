from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page
import re
import pandas as pd

url = "https://www.etsy.com/search?q=gift+for+her&explicit=1&ship_to=ZZ"
data  = requests.get(url).text
soup = BeautifulSoup(data,"html.parser")  # create a soup object using the variable 'data'

list_of_shop = []
for shop in soup.findAll('span',text= re.compile('From shop')):  # in html anchor/link is represented by the tag <a>
    shop_name = shop.getText().replace('From shop', '')
    list_of_shop.append(shop_name)

shop_data = pd.DataFrame(list_of_shop,columns=['shop'])
print(shop_data)