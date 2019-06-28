import urllib2
from bs4 import BeautifulSoup

# Create / open a file called wishlist.txt which will be a CSVfile
f = open("wishlist.txt", "w")

url = raw_input('Enter the URL of your public Amazon Wish List: ')

# Open amazon.com url
print "Getting data for your wish list!"
page = urllib2.urlopen(url)

# Get data from page
soup = BeautifulSoup(page, "html.parser")
#itemName = soup.findAll(attrs={"class":"a-link-normal a-declarative"})[0].get_text()
itemPrice = soup.findAll(attrs={"class":"a-size-base a-color-price a-text-bold"})
for price in itemPrice:
    print price.get_text()

# Write item name and price to file
f.write(itemPrice)

# Done getting data! Close file.
f.close()
