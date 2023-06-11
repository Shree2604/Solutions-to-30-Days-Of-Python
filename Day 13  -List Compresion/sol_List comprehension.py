# Filter only negative and zero numbers in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered_numbers = [num for num in numbers if num <= 0]
print(filtered_numbers)

# Flatten the list of lists of lists to a one-dimensional list
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [num for sublist in list_of_lists for subsublist in sublist for num in subsublist]
print(flattened_list)

# Create the list of tuples using list comprehension
list_of_tuples = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print(list_of_tuples)

# Flatten the list to a new list
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

flattened_list = [[country[0].upper(), country[0][:3].upper(), country[1].upper()] for sublist in countries for country in sublist]

print(flattened_list)


# Change the list to a list of dictionaries
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
dict_list = [{'country': country[0][0].upper(), 'city': country[0][1]} for country in countries]
print(dict_list)

# Change the list of lists to a list of concatenated strings
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concatenated_list = [' '.join(name[0]) for name in names]
print(concatenated_list)

# Lambda function to solve slope or y-intercept of linear functions
slope = lambda x, m, c: m*x + c
y_intercept = lambda m, c: c
