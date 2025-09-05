from bs4 import BeautifulSoup
import requests
import pandas as pd
url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')
print(soup.prettify())
table = soup.find('table')
print(table.prettify() if table else "No table found")
world_titles = table.find_all('th')
print(world_titles)
world_table_titles = [title.text for title in world_titles]
print(world_table_titles)
df = pd.DataFrame(columns=world_table_titles)
print(df)
column_data = table.find_all('tr')
print(column_data)
for row in column_data[1:]:
    row_data = row.find_all('td')
    row_data = row.find_all('td')
    individual_row_data = [row.text.strip() for data in row_data]
    print(individual_row_data)
    length = len(df)
    df.loc[length] = individual_row_data
print(df)
df.to_csv('us_companies.csv', index=False)
