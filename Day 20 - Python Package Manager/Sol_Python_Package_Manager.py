import requests
import json
import statistics
from bs4 import BeautifulSoup

# Read and find the 10 most frequent words from Romeo and Juliet
romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
response = requests.get(romeo_and_juliet)
text = response.text
words = text.split()
word_counts = {}

for word in words:
    if word not in word_counts:
        word_counts[word] = 1
    else:
        word_counts[word] += 1

frequent_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:10]

print("10 most frequent words in Romeo and Juliet:")
for word, count in frequent_words:
    print(word, "-", count)
print()

# Read and find the weight and lifespan statistics of cats from the API
cats_api = 'https://api.thecatapi.com/v1/breeds'
response = requests.get(cats_api)
breeds = json.loads(response.text)

weights = [breed['weight']['metric'] for breed in breeds if 'weight' in breed]
weights = [float(w.split()[0]) for w in weights]
weights_min = min(weights)
weights_max = max(weights)
weights_mean = statistics.mean(weights)
weights_median = statistics.median(weights)
weights_std = statistics.stdev(weights)

lifespans = [breed['life_span'] for breed in breeds if 'life_span' in breed]
lifespans = [float(l.split()[0]) for l in lifespans]
lifespans_min = min(lifespans)
lifespans_max = max(lifespans)
lifespans_mean = statistics.mean(lifespans)
lifespans_median = statistics.median(lifespans)
lifespans_std = statistics.stdev(lifespans)

print("Weight Statistics:")
print("Min:", weights_min)
print("Max:", weights_max)
print("Mean:", weights_mean)
print("Median:", weights_median)
print("Standard Deviation:", weights_std)
print()

print("Lifespan Statistics:")
print("Min:", lifespans_min)
print("Max:", lifespans_max)
print("Mean:", lifespans_mean)
print("Median:", lifespans_median)
print("Standard Deviation:", lifespans_std)
print()

# Create a frequency table of country and breed of cats
frequency_table = {}
for breed in breeds:
    if 'country' in breed:
        country = breed['country']
        name = breed['name']
        key = (country, name)
        if key not in frequency_table:
            frequency_table[key] = 1
        else:
            frequency_table[key] += 1

print("Frequency Table of Country and Breed:")
for (country, breed), count in frequency_table.items():
    print(f"{country} - {breed}: {count}")
print()

# Read and find the 10 largest countries from the countries API
countries_api = 'https://restcountries.com/v3.1/all'
response = requests.get(countries_api)
countries = json.loads(response.text)

largest_countries = sorted(countries, key=lambda c: c['area'], reverse=True)[:10]
print("10 Largest Countries:")
for country in largest_countries:
    print(country['name']['official'], "-", country['area'], "km²")
print()

# Find the 10 most spoken languages in the countries API
languages_counter = {}
for country in countries:
    if 'languages' in country:
        languages = country['languages']
        for language in languages:
            if language not in languages_counter:
                languages_counter[language] = 1
            else:
                languages_counter[language] += 1

most_spoken_languages = sorted(languages_counter.items(), key=lambda x: x[1], reverse=True)[:10]
print("10 Most Spoken Languages:")
for language, count in most_spoken_languages:
    print(language, "-", count)
print()

# Find the total number of languages in the countries API
total_languages = len(languages_counter)
print("Total Number of Languages:", total_languages)
print()

# Read the content of UCI and extract data sets using BeautifulSoup4
uci_url = 'https://archive.ics.uci.edu/ml/datasets.php'
response = requests.get(uci_url)
soup = BeautifulSoup(response.text, 'html.parser')
datasets = soup.find_all('p', class_='normal')
dataset_names = [dataset.text.strip() for dataset in datasets]
print("UCI Dataset Names:")
for name in dataset_names:
    print(name)


