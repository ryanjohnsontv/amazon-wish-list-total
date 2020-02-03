from bs4 import BeautifulSoup
from urllib.request import urlopen
from re import sub
from decimal import Decimal

sum = 0

# Prompt user for wish list URL
url = input('Enter the URL of your public Amazon Wish List: ')

# Open URL
page = urllib.request.urlopen(url)

# Parse data from page
soup = BeautifulSoup(page, "html.parser")
itemPrice = soup.findAll(attrs={"class":"a-offscreen"})

# Parse item prices, format as float variable and add to sum to find total cost
for price in itemPrice:
    value = price.get_text()
    valueItem = Decimal(sub(r'[^\d.]', '', value))
    sum = sum + valueItem
    
# Print item total, formatted with U.S. current ($)
print('Wish List Total: ' + '${}'.format(sum))
