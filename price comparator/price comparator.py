import requests
from bs4 import BeautifulSoup


custprint_product_url ="https://www.custprint.com/luxe-round-neck-cotton-tee.html"
headers= "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
page = requests.get(url=custprint_product_url, headers=headers)
soup = BeautifulSoup(page.content,'html')
print(soup.prettify())
title = soup.find(id = 'title')
text = title.get_text() # Will get text from html tags
product_title = text.strip() # Removing special characters like \n (newline)
print(product_title )
price = soup.find(id = 'priceblock_ourprice')
price = price.get_text() # Will get text from html tags
amazon_product_price = price.strip() # Removing special characters like \n (newline)
print(custprint_product_price )