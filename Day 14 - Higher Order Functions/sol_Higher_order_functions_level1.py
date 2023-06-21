## Exercises: Level 1

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1 Explain the difference between map, filter, and reduce.

map, filter, and reduce are all functions that bring a bit of functional programming to Python. 
All three of these are convenience functions that can be replaced with List Comprehensions or loops,
but provide a more elegant and short-hand approach to some problems.

map creates a new array by transforming every element in an array individually.
filter creates a new array by removing elements that don’t belongreduce,
on the other hand, reduce takes all of the elements in an array and reduces them into a single value.

# 2 Explain the difference between higher order function, closure and decorator
A higher-order function is a function that either takes a function as an argument or returns a function.
A closure gives access to an outer function’s scope from an inner function. Closures are commonly used to give objects data privacy.
A decorator is the extension of a Python higher order function and closure. It takes another function as an argument and decorates it without altering any functionality of the certain function. 

# 3 Define a call function before map, filter or reduce, see examples.
def square(x):
    return x * x

numbers = [1, 2, 3, 4]
squared_numbers = map(square, numbers)
print(list(squared_numbers)) # [1, 4, 9, 16]

def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4]
even_numbers = filter(is_even, numbers)
print(list(even_numbers)) # [2, 4]

from functools import reduce

def add(x, y):
    return x + y

numbers = [1, 2, 3, 4]
sum_of_numbers = reduce(add, numbers)
print(sum_of_numbers) # 10


# 4 Use for loop to print each country in the countries list.

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
for country in countries:
    print(country)

# In list comprehension it can be written as
[print(i) for i in countries ]



# 5 Use for to print each name in the names list.

names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
for name in names:
    print(name)


# 6 Use for to print each number in the numbers list.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    print(number)




  
