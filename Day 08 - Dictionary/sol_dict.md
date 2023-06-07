# Question 1: Create an empty dictionary called dog
dog = {}

# Question 2: Add name, color, breed, legs, age to the dog dictionary
dog = {
    'name': 'Buddy',
    'color': 'brown',
    'breed': 'Labrador Retriever',
    'legs': 4,
    'age': 5
}

# Question 3: Create a student dictionary and add various keys and values
student = {
    'first_name': 'John',
    'last_name': 'Doe',
    'gender': 'Male',
    'age': 25,
    'marital_status': 'Single',
    'skills': ['Python', 'Java', 'C++'],
    'country': 'USA',
    'city': 'New York',
    'address': '123 Main St'
}

# Question 4: Get the length of the student dictionary
len(student)

# Question 5: Get the value of skills and check the data type
skills = student['skills']
type(skills)  # Should return <class 'list'>

# Question 6: Modify the skills values by adding one or two skills
student['skills'].append('JavaScript')
student['skills'].append('HTML')

# Question 7: Get the dictionary keys as a list
list(student.keys())

# Question 8: Get the dictionary values as a list
list(student.values())

# Question 9: Change the dictionary to a list of tuples using items() method
list(student.items())

# Question 10: Delete one of the items in the dictionary
del student['address']

# Question 11: Delete the student dictionary
del student  # This will delete the entire student dictionary.
