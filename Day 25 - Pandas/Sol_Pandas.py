import pandas as pd

# 1. Read the hacker_news.csv file from data directory
df = pd.read_csv('data/hacker_news.csv')

# 2. Get the first five rows
first_five_rows = df.head()

# 3. Get the last five rows
last_five_rows = df.tail()

# 4. Get the title column as pandas series
title_column = df['title']

# 5. Count the number of rows and columns
num_rows, num_columns = df.shape

# Filter the titles which contain python
python_titles = df[df['title'].str.contains('python', case=False)]

# Filter the titles which contain JavaScript
javascript_titles = df[df['title'].str.contains('JavaScript', case=False)]

# Explore the data and make sense of it
