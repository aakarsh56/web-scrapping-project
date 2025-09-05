import requests
from bs4 import BeautifulSoup
url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
soup = BeautifulSoup(requests.get(url).content, 'html.parser')
print(soup.prettify())
