# 1. Declare an empty list
my_list = []

# 2. Declare a list with more than 5 items
my_list = [1, 2, 3, 4, 5, 6]

# 3. Find the length of your list
len(my_list)

# 4. Get the first item, the middle item, and the last item of the list
first_item = my_list[0]
middle_item = my_list[len(my_list)//2]
last_item = my_list[-1]

# 5. Declare a list called mixed_data_types and store your name, age, height, marital status, and address
mixed_data_types = ['John Doe', 25, 1.75, 'Single', '123 Main St']

# 6. Declare a list variable named it_companies and assign initial values: Facebook, Google, Microsoft, Apple, IBM, Oracle, and Amazon
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7. Print the list using print()
print(it_companies)

# 8. Print the number of companies in the list
print(len(it_companies))

# 9. Print the first, middle, and last company
print(it_companies[0])
print(it_companies[len(it_companies)//2])
print(it_companies[-1])

# 10. Print the list after modifying one of the companies
it_companies[0] = 'New Company'
print(it_companies)

# 11. Add an IT company to it_companies
it_companies.append('New Company')

# 12. Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies)//2, 'New Company')

# 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0] = it_companies[0].upper()

# 14. Join the it_companies with the string '#; '
joined_string = '#; '.join(it_companies)

# 15. Check if a certain company exists in the it_companies list
'Google' in it_companies  # Returns True if Google is in the list.

# 16. Sort the list using the sort() method
it_companies.sort()

# 17. Reverse the list in descending order using the reverse() method
it_companies.reverse()

# 18. Slice out the first 3 companies from the list
first_3 = it_companies[:3]

# 19. Slice out the last 3 companies from the list
last_3 = it_companies[-3:]

# 20. Slice out the middle IT company or companies from the list
middle_company = it_companies[len(it_companies)//2]

# 21. Remove the first IT company from the list
it_companies.pop(0)

# 22. Remove the middle IT company or companies from the list
it_companies.pop(len(it_companies)//2)

# 23. Remove the last IT company from the list
it_companies.pop(-1)

# 24. Remove all IT companies from the list
it_companies.clear()

# 25. Destroy the IT companies list
del it_companies

# 26. Join the following lists: front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux'], back_end = ['Node', 'Express', 'MongoDB']
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end

# 27. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = front_end + back_end
full_stack.insert(full_stack.index('Redux') + 1, 'Python')
full_stack.insert(full_stack.index('Python') + 1, 'SQL')
