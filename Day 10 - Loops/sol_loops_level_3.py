# Loop through the countries and extract countries containing the word 'land'
from data.countries import countries

land_countries = []

for country in countries:
    if 'land' in country.lower():
        land_countries.append(country)

print(land_countries)

# Reverse the order of the fruit list using a loop
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []

for i in range(len(fruits)-1, -1, -1):
    reversed_fruits.append(fruits[i])

print(reversed_fruits)

# Total number of languages in the data
from data.countries_data import countries_data

languages = set()

for country in countries_data:
    languages.update(country['languages'])

total_languages = len(languages)
print("Total number of languages:", total_languages)

# Ten most spoken languages from the data
language_count = {}

for country in countries_data:
    for language in country['languages']:
        if language in language_count:
            language_count[language] += 1
        else:
            language_count[language] = 1

top_10_languages = sorted(language_count, key=language_count.get, reverse=True)[:10]
print("Ten most spoken languages:", top_10_languages)

# Ten most populated countries in the world
populated_countries = sorted(countries_data, key=lambda x: x['population'], reverse=True)[:10]

for country in populated_countries:
    print(country['name'])
