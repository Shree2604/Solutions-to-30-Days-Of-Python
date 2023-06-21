from countries_data import countries

# Sort countries by name
countries_sorted_by_name = sorted(countries, key=lambda c: c['name'])
print("Countries sorted by name:")
for country in countries_sorted_by_name:
    print(country['name'])

print("\n")

# Sort countries by capital
countries_sorted_by_capital = sorted(countries, key=lambda c: c['capital'])
print("Countries sorted by capital:")
for country in countries_sorted_by_capital:
    print(country['capital'])

print("\n")

# Sort countries by population
countries_sorted_by_population = sorted(countries, key=lambda c: c['population'], reverse=True)
print("Countries sorted by population:")
for country in countries_sorted_by_population:
    print(country['name'], "Population:", country['population'])

print("\n")

# Get the ten most spoken languages
languages = set()
for country in countries:
    languages.update(country['languages'])
most_spoken_languages = sorted(languages, key=lambda lang: len(lang['speakers']), reverse=True)[:10]
print("Ten most spoken languages by location:")
for language in most_spoken_languages:
    print(language['name'])

print("\n")

# Sort countries by population and get the ten most populated countries
most_populated_countries = sorted(countries, key=lambda c: c['population'], reverse=True)[:10]
print("Ten most populated countries:")
for country in most_populated_countries:
    print(country['name'], "Population:", country['population'])
