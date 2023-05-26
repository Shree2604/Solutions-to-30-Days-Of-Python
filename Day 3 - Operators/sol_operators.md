# Exercise 1: Declare your age as an integer variable
age = 25

# Exercise 2: Declare your height as a float variable
height = 5.7

# Exercise 3: Declare a variable that stores a complex number
complex_num = 2 + 3j

# Exercise 4: Calculate the area of a triangle
base = float(input("Enter base: "))
height = float(input("Enter height: "))
area = 0.5 * base * height
print("The area of the triangle is", area)

# Exercise 5: Calculate the perimeter of a triangle
side_a = float(input("Enter side a: "))
side_b = float(input("Enter side b: "))
side_c = float(input("Enter side c: "))
perimeter = side_a + side_b + side_c
print("The perimeter of the triangle is", perimeter)

# Exercise 6: Calculate the area and perimeter of a rectangle
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
perimeter = 2 * (length + width)
print("The area of the rectangle is", area)
print("The perimeter of the rectangle is", perimeter)

# Exercise 7: Calculate the area and circumference of a circle
radius = float(input("Enter radius: "))
pi = 3.14
area = pi * radius * radius
circumference = 2 * pi * radius
print("The area of the circle is", area)
print("The circumference of the circle is", circumference)

# Exercise 8: Calculate the slope, x-intercept, and y-intercept of y = 2x - 2
slope = 2
x_intercept = 0
y_intercept = -2
print("Slope =", slope)
print("x-intercept =", x_intercept)
print("y-intercept =", y_intercept)

# Exercise 9: Calculate the slope and Euclidean distance between two points
x1, y1 = 2, 2
x2, y2 = 6, 10
slope = (y2 - y1) / (x2 - x1)
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print("Slope =", slope)
print("Distance =", distance)

# Exercise 10: Compare the slopes from Exercises 8 and 9
if slope == 2:
    print("The slopes are equal.")
else:
    print("The slopes are not equal.")

# Exercise 11: Calculate the value of y and find the x value where y is 0
x = -3
y = x ** 2 + 6 * x + 9
print("When x =", x, ", y =", y)

# Exercise 12: Find the length of 'python' and 'dragon' and make a falsy comparison statement
length_python = len('python')
length_dragon = len('dragon')
if length_python == length_dragon:
    print("The lengths are equal.")
else:
    print("The lengths are not equal.")

# Exercise 13: Use the 'and' operator to check if 'on' is found in both 'python' and 'dragon'
if 'on' in 'python' and 'on' in 'dragon':
    print("'on' is found in both 'python' and 'dragon'.")
else:
    print("'on' is not found in both 'python' and 'dragon'.")

# Exercise 14: Use the 'in' operator to check if 'jargon' is in the sentence
sentence = "I hope this course is not full of jargon."
if 'jargon' in sentence:
    print("'jargon' is in the sentence.")
else:
    print("'jargon' is not in the sentence.")

# Exercise 15: Check if a number is even
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# Exercise 16: Check if the floor division of 7 by 3 is equal to the int converted value of 2.7
if 7 // 3 == int(2.7):
    print("The statement is true.")
else:
    print("The statement is false.")

# Exercise 17: Check if the type of '10' is equal to the type of 10
if type('10') == type(10):
    print("The types are equal.")
else:
    print("The types are not equal.")

# Exercise 18: Check if int('9.8') is equal to 10
try:
    if int('9.8') == 10:
        print("The values are equal.")
    else:
        print("The values are not equal.")
except ValueError:
    print("Cannot convert '9.8' to an integer.")

# Exercise 19: Calculate the pay of a person
hours = float(input("Enter hours: "))
rate_per_hour = float(input("Enter rate per hour: "))
earnings = hours * rate_per_hour
print("Your weekly earning is", earnings)

# Exercise 20: Calculate the number of seconds a person can live
years_lived = int(input("Enter number of years you have lived: "))
seconds_per_year = 365 * 24 * 60 * 60
seconds_lived = years_lived * seconds_per_year
print("You have lived for", seconds_lived, "seconds.")

# Exercise 21: Display the table
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")
