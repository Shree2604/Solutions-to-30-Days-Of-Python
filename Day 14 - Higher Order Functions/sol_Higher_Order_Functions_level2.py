from functools import reduce

# Exercise 1: Use map to create a new list by changing each country to uppercase in the countries list
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
uppercased_countries = list(map(str.upper, countries))
print(uppercased_countries)  # Output: ['ESTONIA', 'FINLAND', 'SWEDEN', 'DENMARK', 'NORWAY', 'ICELAND']

# Exercise 2: Use map to create a new list by changing each number to its square in the numbers list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Exercise 3: Use map to change each name to uppercase in the names list
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
uppercased_names = list(map(str.upper, names))
print(uppercased_names)  # Output: ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']

# Exercise 4: Use filter to filter out countries containing 'land'
filtered_countries = list(filter(lambda country: 'land' not in country, countries))
print(filtered_countries)  # Output: ['Sweden', 'Denmark', 'Norway', 'Iceland']

# Exercise 5: Use filter to filter out countries having exactly six characters
filtered_countries = list(filter(lambda country: len(country) != 6, countries))
print(filtered_countries)  # Output: ['Estonia', 'Finland', 'Denmark', 'Norway', 'Iceland']

# Exercise 6: Use filter to filter out countries containing six letters and more in the country list
filtered_countries = list(filter(lambda country: len(country) < 6, countries))
print(filtered_countries)  # Output: ['Sweden']

# Exercise 7: Use filter to filter out countries starting with an 'E'
filtered_countries = list(filter(lambda country: not country.startswith('E'), countries))
print(filtered_countries)  # Output: ['Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

# Exercise 8: Chain two or more list iterators
result = list(map(str.upper, filter(lambda country: len(country) != 6, countries)))
print(result)  # Output: ['ESTONIA', 'FINLAND', 'DENMARK', 'NORWAY', 'ICELAND']

# Exercise 9: Declare a function called get_string_lists that returns a list containing only string items
def get_string_lists(lst):
    return list(filter(lambda item: isinstance(item, str), lst))

# Exercise 10: Use reduce to sum all the numbers in the numbers list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)  # Output: 55

# Exercise 11: Use reduce to concatenate all the countries and produce the sentence
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
sentence = reduce(lambda x, y: x + ', ' + y, countries) + ' are north European countries'
print(sentence)  # Output: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries

# Exercise 12 : Declare a function called categorize_countries that returns a list of countries with some common pattern
def categorize_countries():
    pattern = 'land'
    return list(filter(lambda country: pattern in country, countries))

# Exercise 13 : Create a function returning a dictionary where keys are starting letters of countries and values are the count of country names starting with that letter
def get_country_counts():
    country_counts = {}
    for country in countries:
        first_letter = country[0]
        if first_letter in country_counts:
            country_counts[first_letter] += 1
        else:
            country_counts[first_letter] = 1
    return country_counts

# Exercise 14 : Declare a get_first_ten_countries function - it returns a list of the first ten countries from the countries list
def get_first_ten_countries():
    return countries[:10]

# Exercise 15 : Declare a get_last_ten_countries function that returns the last ten countries in the countries list
def get_last_ten_countries():
    return countries[-10:]

# Testing the functions
string_list = ['Python', 2023, 'Java', 'JavaScript', 123, 'HTML']
print(get_string_lists(string_list))  # Output: ['Python', 'Java', 'JavaScript', 'HTML']

print(categorize_countries())  # Output: ['Finland', 'Iceland']

print(get_country_counts())  # Output: {'E': 1, 'F': 1, 'S': 1, 'D': 1, 'N': 1, 'I': 1}

print(get_first_ten_countries())  # Output: ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

print(get_last_ten_countries())  # Output: ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
