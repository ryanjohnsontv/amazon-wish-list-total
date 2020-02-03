from bs4 import BeautifulSoup
from urllib.request import urlopen
from re import sub
from decimal import Decimal

# Create / open a file called wishlist.txt which will be a CSVfile
f = open("wishlist.txt", "w")

url = input('Enter the URL of your public Amazon Wish List: ')

# Open amazon.com url
print ("Getting data for your wish list!")
page = urllib.request.urlopen(url)

# Get data from page
soup = BeautifulSoup(page, "html.parser")
#itemName = soup.findAll(attrs={"class":"a-link-normal a-declarative"})[0].get_text()
itemPrice = soup.findAll(attrs={"class":"a-offscreen"})
sum=0
for price in itemPrice:
    value = price.get_text()
    valueItem = Decimal(sub(r'[^\d.]', '', value))
    #print (valueItem)
    sum = sum + valueItem

# Write item name and price to file
f.write(str(itemPrice))

print(sum)

# Done getting data! Close file.
f.close()
