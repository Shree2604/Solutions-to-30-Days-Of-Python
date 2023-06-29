import requests
import json
from bs4 import BeautifulSoup
import pandas as pd

# 1. Scraping the website 'http://www.bu.edu/president/boston-university-facts-stats/' and storing the data as a JSON file

bu_url = 'http://www.bu.edu/president/boston-university-facts-stats/'

# Send a GET request to the URL
response = requests.get(bu_url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table element on the page
table = soup.find('table')

# Create a list to store the table data
bu_data = []

# Extract the table headers
headers = [th.text.strip() for th in table.find_all('th')]

# Extract the table rows
for row in table.find_all('tr'):
    cells = [cell.text.strip() for cell in row.find_all('td')]
    if cells:
        bu_data.append(dict(zip(headers, cells)))

# Store the BU data as JSON
with open('bu_data.json', 'w') as json_file:
    json.dump(bu_data, json_file, indent=4)


# 2. Extracting the table from 'https://archive.ics.uci.edu/ml/datasets.php' and converting it to a JSON file

uci_url = 'https://archive.ics.uci.edu/ml/datasets.php'

# Send a GET request to the URL
response = requests.get(uci_url)

# Use pandas to read the HTML table
tables = pd.read_html(response.content)

# Assuming the desired table is the first one on the page
table = tables[0]

# Convert the table to a JSON object
uci_data = table.to_json(orient='records')

# Store the UCI dataset as JSON
with open('uci_dataset.json', 'w') as json_file:
    json_file.write(uci_data)


# 3. Scraping the presidents table from 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'

presidents_url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'

# Send a GET request to the URL
response = requests.get(presidents_url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table element on the page
table = soup.find('table', class_='wikitable')

# Create a list to store the table data
presidents_data = []

# Extract the table rows
rows = table.find_all('tr')

# Extract the table headers
headers = [header.text.strip() for header in rows[0].find_all('th')]

# Extract the table data
for row in rows[1:]:
    cells = [cell.text.strip() for cell in row.find_all('td')]
    presidents_data.append(dict(zip(headers, cells)))

# Store the presidents data as JSON
with open('presidents_data.json', 'w') as json_file:
    json.dump(presidents_data, json_file, indent=4)
