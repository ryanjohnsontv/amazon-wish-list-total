import urllib
from bs4 import BeautifulSoup

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
for price in itemPrice:
    print (price.get_text())

# Write item name and price to file
f.write(str(itemPrice))

# Done getting data! Close file.
f.close()
