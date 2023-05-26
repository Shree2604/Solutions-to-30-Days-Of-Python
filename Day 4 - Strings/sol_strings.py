# Exercise 1
concatenated_string = 'Thirty' + ' Days' + ' Of' + ' Python'
print(concatenated_string)

# Exercise 2
concatenated_string = 'Coding' + ' For' + ' All'
print(concatenated_string)

# Exercise 3
company = "Coding For All"
print(company)

# Exercise 4
print(company)

# Exercise 5
print(len(company))

# Exercise 6
print(company.upper())

# Exercise 7
print(company.lower())

# Exercise 8
print(company.capitalize())
print(company.title())
print(company.swapcase())

# Exercise 9
sliced_string = company[7:]
print(sliced_string)

# Exercise 10
print('Coding' in company)

# Exercise 11
replaced_string = company.replace('Coding', 'Python')
print(replaced_string)

# Exercise 12
replaced_string = company.replace('Everyone', 'All')
print(replaced_string)

# Exercise 13
split_string = company.split()
print(split_string)

# Exercise 14
comma_separated_string = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
split_string = comma_separated_string.split(', ')
print(split_string)

# Exercise 15
print(company[0])

# Exercise 16
print(company.rindex(' '))
print(len(company) - 1)

# Exercise 17
print(company[10])

# Exercise 18
name = 'Python For Everyone'
acronym = ''.join(word[0] for word in name.split())
print(acronym)

# Exercise 19
name = 'Coding For All'
acronym = ''.join(word[0] for word in name.split())
print(acronym)

# Exercise 20
print(company.index('C'))

# Exercise 21
print(company.index('F'))

# Exercise 22
print(company.rfind('l'))

# Exercise 23
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))

# Exercise 24
print(sentence.rindex('because'))

# Exercise 25
phrase = 'because because because'
print(sentence[sentence.index(phrase):sentence.index(phrase) + len(phrase)])

# Exercise 26
print(sentence.index('because'))

# Exercise 27
print(sentence[sentence.index(phrase):sentence.index(phrase) + len(phrase)])

# Exercise 28
print(company.startswith('Coding'))

# Exercise 29
print(company.endswith('coding'))

# Exercise 30
string_with_spaces = '   Coding For All      '
print(string_with_spaces.strip())

# Exercise 31
var1 = '30DaysOfPython'
var2 = 'thirty_days_of_python'
print(var1.isidentifier())
print(var2.isidentifier())

# Exercise 32
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_string = ' # '.join(libraries)
print(joined_string)

# Exercise 33
sentences = "I am enjoying this challenge.\nI just wonder what is next."
print(sentences)

# Exercise 34
lines = "Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki"
print(lines)

# Exercise 35
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")

# Exercise 36
result = f"8 + 6 = {8 + 6}\n8 - 6 = {8 - 6}\n8 * 6 = {8 * 6}\n8 / 6 = {8 / 6}\n8 % 6 = {8 % 6}\n8 // 6 = {8 // 6}\n8 ** 6 = {8 ** 6}"
print(result)
