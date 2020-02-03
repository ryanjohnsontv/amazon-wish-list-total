from bs4 import BeautifulSoup
from urllib.request import urlopen
from re import sub
from decimal import Decimal

sum = 0

url = input('Enter the URL of your public Amazon Wish List: ')

# Open amazon.com url
print ("Getting data for your wish list!")
page = urllib.request.urlopen(url)

# Get data from page
soup = BeautifulSoup(page, "html.parser")
itemPrice = soup.findAll(attrs={"class":"a-offscreen"})

for price in itemPrice:
    value = price.get_text()
    valueItem = Decimal(sub(r'[^\d.]', '', value))
    #print (valueItem)
    sum = sum + valueItem

print(sum)
