# Level 1
# Question 1: Find the length of the set it_companies
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
len(it_companies)

# Question 2: Add ‘Twitter’ to it_companies
it_companies.add('Twitter')

# Question 3: Insert multiple IT companies at once to the set it_companies
it_companies.update(['Meta', 'Netflix'])

# Question 4: Remove one of the companies from the set it_companies
it_companies.remove('Facebook')

# Question 5: What is the difference between remove and discard?
# The remove method removes a specified element from a set. If the element is not found in the set, it raises a KeyError.
# The discard method also removes a specified element from a set, but if the element is not found in the set, it does not raise an error.


# Level 2
# Question 6: Join A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
A.union(B)

# Question 7: Find A intersection B
A.intersection(B)

# Question 8: Is A subset of B
A.issubset(B)

# Question 9: Are A and B disjoint sets
A.isdisjoint(B)

# Question 10: Join A with B and B with A
A.update(B)
B.update(A)

# Question 11: What is the symmetric difference between A and B
A.symmetric_difference(B)

# Question 12: Delete the sets completely
del A
del B


# Level 3
# Question 13: Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age = [22, 19, 24, 25, 26, 24, 25, 24]
age_set = set(age)
if len(age) > len(age_set):
    print("The list is bigger")
else:
    print("The set is bigger")
   # Answer : The list is bigger
  
  

# Question 14: Explain the difference between the following data types: string, list, tuple, and set
# String: A string is a sequence of characters enclosed in quotation marks.
# List: A list is an ordered collection of elements enclosed in square brackets. Lists are mutable, which means their elements can be changed.
# Tuple: A tuple is an ordered collection of elements enclosed in parentheses. Tuples are immutable, which means their elements cannot be changed.
# Set: A set is an unordered collection of unique elements enclosed in curly braces.

# Question 15: How many unique words have been used in the sentence? Use the split method and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people"
words = sentence.split()
unique_words = set(words)
num_unique_words = len(unique_words)
