# Level 1

# Question 1
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    years_left = 18 - age
    print("You need", years_left, "more years to learn to drive.")

# Question 2
your_age = int(input("Enter your age: "))
if your_age > my_age:
    age_difference = your_age - my_age
    if age_difference == 1:
        print("You are", age_difference, "year older than me.")
    else:
        print("You are", age_difference, "years older than me.")
elif your_age < my_age:
    age_difference = my_age - your_age
    if age_difference == 1:
        print("I am", age_difference, "year older than you.")
    else:
        print("I am", age_difference, "years older than you.")
else:
    print("We are the same age.")

# Question 3
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))
if a > b:
    print(a, "is greater than", b)
elif a < b:
    print(a, "is smaller than", b)
else:
    print("Both numbers are equal.")

# Level 2

# Question 1
score = int(input("Enter your score: "))
if score >= 80 and score <= 100:
    print("A")
elif score >= 70 and score <= 89:
    print("B")
elif score >= 60 and score <= 69:
    print("C")
elif score >= 50 and score <= 59:
    print("D")
elif score >= 0 and score <= 49:
    print("F")
else:
    print("Invalid score")

# Question 2
month = input("Enter a month: ")
if month in ['September', 'October', 'November']:
    print("Autumn")
elif month in ['December', 'January', 'February']:
    print("Winter")
elif month in ['March', 'April', 'May']:
    print("Spring")
elif month in ['June', 'July', 'August']:
    print("Summer")
else:
    print("Invalid month")

# Question 3
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Enter a fruit: ")
if fruit in fruits:
    print("That fruit already exists in the list")
else:
    fruits.append(fruit)
    print("Modified list:", fruits)

# Level 3

# Question 1
if 'skills' in person:
    skills = person['skills']
    middle_skill = skills[len(skills)//2]
    print("Middle skill:", middle_skill)

# Question 2
if 'skills' in person:
    if 'Python' in person['skills']:
        print("The person has the 'Python' skill")

# Question 3
if 'skills' in person:
    skills = person['skills']
    if 'JavaScript' in skills and 'React' in skills:
        print("He is a front end developer")
    elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
        print("He is a backend developer")
    elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
        print("He is a fullstack developer")
    else:
        print("Unknown title")

# Question 4
if person.get('is_married') and person.get('country') == 'Finland':
    print(person['first_name'], person['last_name'], "lives in", person['country'] + ". He is married.")
