# Level 1

# 1. Declare a function add_two_numbers. It takes two parameters and it returns the sum.
def add_two_numbers(num1, num2):
    return num1 + num2


# 2. Write a function that calculates the area of a circle.
#    The formula for calculating the area of a circle is: area = π x r x r
def area_of_circle(radius):
    import math
    return math.pi * radius * radius


# 3. Write a function called add_all_nums which takes an arbitrary number of arguments and sums all the arguments.
#    Check if all the list items are number types. If not, give a reasonable feedback.
def add_all_nums(*args):
    total = 0
    for num in args:
        if isinstance(num, (int, float)):
            total += num
        else:
            return "Invalid input: All list items should be numbers."
    return total


# 4. Write a function which converts temperature in °C to °F.
#    The formula for converting °C to °F is: °F = (°C x 9/5) + 32
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


# 5. Write a function called check_season which takes a month parameter and returns the season: Autumn, Winter, Spring, or Summer.
def check_season(month):
    if month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    elif month in [9, 10, 11]:
        return "Autumn"
    else:
        return "Winter"


# 6. Write a function called calculate_slope which returns the slope of a linear equation.
def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)


# 7. Write a function which calculates the solution set of a quadratic equation.
#    The quadratic equation is calculated as follows: ax² + bx + c = 0
def solve_quadratic_eqn(a, b, c):
    import cmath
    discriminant = (b**2) - (4*a*c)
    sol1 = (-b - cmath.sqrt(discriminant)) / (2*a)
    sol2 = (-b + cmath.sqrt(discriminant)) / (2*a)
    return sol1, sol2


# 8. Declare a function named print_list. It takes a list as a parameter and prints out each element of the list.
def print_list(lst):
    for item in lst:
        print(item)


# 9. Declare a function named reverse_list. It takes an array as a parameter and returns the reverse of the array (use loops).
def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst)-1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst


# 10. Declare a function named capitalize_list_items. It takes a list as a parameter and returns a capitalized list of items.
def capitalize_list_items(lst):
    capitalized_lst = []
    for item in lst:
        capitalized_lst.append(item.capitalize())
    return capitalized_lst


# 11. Declare a function named add_item. It takes a list and an item as parameters.
#     It returns a list with the item added at the end.
def add_item(lst, item):
    lst.append(item)
    return lst


# 12. Declare a function named remove_item. It takes a list and an item as parameters.
#     It returns a list with the item removed from it.
def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst


# 13. Declare a function named sum_of_numbers. It takes a number as a parameter and adds all the numbers in that range.
def sum_of_numbers(num):
    total = 0
    for i in range(1, num+1):
        total += i
    return total


# 14. Declare a function named sum_of_odds. It takes a number as a parameter and adds all the odd numbers in that range.
def sum_of_odds(num):
    total = 0
    for i in range(1, num+1):
        if i % 2 != 0:
            total += i
    return total


# 15. Declare a function named sum_of_even. It takes a number as a parameter and adds all the even numbers in that range.
def sum_of_even(num):
    total = 0
    for i in range(1, num+1):
        if i % 2 == 0:
            total += i
    return total


# Level 2

# 1. Declare a function named evens_and_odds. It takes a positive integer as a parameter
#    and counts the number of evens and odds in the number.
def evens_and_odds(num):
    evens = 0
    odds = 0
    for digit in str(num):
        if int(digit) % 2 == 0:
            evens += 1
        else:
            odds += 1
    return f"The number of odds are {odds}.\nThe number of evens are {evens}."


# 2. Define a function named factorial. It takes a whole number as a parameter and returns its factorial.
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)


# 3. Define a function named is_empty. It takes a parameter and checks if it is empty or not.
def is_empty(data):
    if data:
        return False
    else:
        return True


# 4. Define different functions which take lists.
#    They should calculate_mean, calculate_median, calculate_mode, calculate_range,
#    calculate_variance, and calculate_std (standard deviation).

# Function to calculate the mean of a list
def calculate_mean(lst):
    return sum(lst) / len(lst)


# Function to calculate the median of a list
def calculate_median(lst):
    sorted_lst = sorted(lst)
    length = len(sorted_lst)
    if length % 2 == 0:
        return (sorted_lst[length//2 - 1] + sorted_lst[length//2]) / 2
    else:
        return sorted_lst[length//2]


# Function to calculate the mode of a list
def calculate_mode(lst):
    from collections import Counter
    count_dict = Counter(lst)
    max_count = max(count_dict.values())
    mode = [num for num, count in count_dict.items() if count == max_count]
    return mode


# Function to calculate the range of a list
def calculate_range(lst):
    return max(lst) - min(lst)


# Function to calculate the variance of a list
def calculate_variance(lst):
    mean = calculate_mean(lst)
    squared_diffs = [(num - mean) ** 2 for num in lst]
    variance = sum(squared_diffs) / len(lst)
    return variance


# Function to calculate the standard deviation of a list
def calculate_std(lst):
    import math
    variance = calculate_variance(lst)
    std_deviation = math.sqrt(variance)
    return std_deviation


# Level 3

# 1. Write a function called is_prime, which checks if a number is prime.
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


# 2. Write a function which checks if all items in a list are unique.
def are_all_items_unique(lst):
    return len(lst) == len(set(lst))


# 3. Write a function which checks if all the items of a list are of the same data type.
def are_all_items_same_type(lst):
    return all(isinstance(item, type(lst[0])) for item in lst)


# 4. Write a function which checks if the provided variable is a valid Python variable name.
def is_valid_variable_name(variable):
    import re
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    if re.match(pattern, variable):
        return True
    else:
        return False


# 5. Go to the data folder and access the countries-data.py file.
#    Create a function called most_spoken_languages_in_the_world.
#    It should return the 10 or 20 most spoken languages in the world in descending order.

def most_spoken_languages_in_the_world():
    from data.countries_data import countries
    all_languages = []
    for country in countries:
        if 'languages' in country:
            all_languages.extend(country['languages'])

    language_count = {}
    for language in all_languages:
        if language in language_count:
            language_count[language] += 1
        else:
            language_count[language] = 1

    sorted_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)
    return [language for language, count in sorted_languages[:20]]


# Create a function called most_populated_countries.
# It should return the 10 or 20 most populated countries in descending order.

def most_populated_countries():
    from data.countries_data import countries
    sorted_countries = sorted(countries, key=lambda x: x['population'], reverse=True)
    return [country['name'] for country in sorted_countries[:20]]
