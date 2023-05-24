## Exercise 1: Declare your age as an integer variable

age = 25

In this exercise, we declare a variable named age and assign it the value of 25. The variable age is of type integer.


## Exercise 2: Declare your height as a float variable

height = 5.7

Here, we declare a variable named height and assign it the value of 5.7. The variable height is of type float.


## Exercise 3: Declare a variable that stores a complex number

complex_num = 2 + 3j

In this exercise, we declare a variable named complex_num and assign it the value of 2 + 3j. The variable complex_num stores a complex number.


## Exercise 4: Calculate the area of a triangle

base = float(input("Enter base: "))

height = float(input("Enter height: "))

area = 0.5 * base * height

print("The area of the triangle is", area)

Here, we prompt the user to enter the base and height of a triangle using the input() function. The values are converted to float using float() for calculation purposes. We then calculate the area of the triangle using the formula 0.5 * base * height and store it in the variable area. Finally, we print the calculated area.

## Exercise 5: Calculate the perimeter of a triangle

side_a = float(input("Enter side a: "))

side_b = float(input("Enter side b: "))

side_c = float(input("Enter side c: "))

perimeter = side_a + side_b + side_c

print("The perimeter of the triangle is", perimeter)

In this exercise, we ask the user to enter the lengths of the three sides of a triangle. The inputs are converted to float using float(). We then calculate the perimeter by adding the lengths of the three sides together and store the result in the variable perimeter. Finally, we display the calculated perimeter.


## Exercise 6: Calculate the area and perimeter of a rectangle

length = float(input("Enter length: "))

width = float(input("Enter width: "))

area = length * width

perimeter = 2 * (length + width)

print("The area of the rectangle is", area)

print("The perimeter of the rectangle is", perimeter)

Here, we prompt the user to enter the length and width of a rectangle. The inputs are converted to float using float(). We then calculate the area of the rectangle by multiplying the length and width and store it in the variable area. Similarly, we calculate the perimeter by using the formula 2 * (length + width) and store it in the variable perimeter. Finally, we display the calculated area and perimeter.


## Exercise 7: Calculate the area and circumference of a circle

radius = float(input("Enter radius: "))

pi = 3.14

area = pi * radius * radius

circumference = 2 * pi * radius

print("The area of the circle is", area)

print("The circumference of the circle is", circumference)

In this exercise, we ask the user to enter the radius of a circle. The input is converted to float using float(). We then calculate the area of the circle using the formula pi * radius * radius, where pi is approximately 3.14. The calculated area is stored in the variable 



## Exercise 8: Calculate the slope, x-intercept, and y-intercept of a linear equation

slope = 2

x_intercept = -1

y_intercept = -2

Here, we declare three variables: slope, x_intercept, and y_intercept. These variables represent the slope, x-intercept, and y-intercept of a linear equation, respectively.

## Exercise 9: Calculate the slope and Euclidean distance between two points

x1, y1 = 2, 2

x2, y2 = 6, 10

slope = (y2 - y1) / (x2 - x1)

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print("The slope is", slope)

print("The Euclidean distance is", distance)



In this exercise, we have two points: (x1, y1) = (2, 2) and (x2, y2) = (6, 10). We calculate the slope using the formula (y2 - y1) / (x2 - x1) and store it in the variable slope. Similarly, we calculate the Euclidean distance between the two points using the formula ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 and store it in the variable distance. Finally, we display the calculated slope and Euclidean distance.


## Exercise 10: Compare the slopes from exercises 8 and 9

if slope == 2:
    print("The slopes are equal.")
else:
    print("The slopes are not equal.")

Here, we compare the slope calculated in exercise 8 (assigned to the variable slope) with the slope calculated in exercise 9. If the slopes are equal, we print "The slopes are equal." Otherwise, we print "The slopes are not equal."


## Exercise 11: Calculate the value of y for a given equation

x = float(input("Enter a value for x: "))
y = x ** 2 + 6 * x + 9
print("The value of y is", y)

In this exercise, we ask the user to enter a value for x. The input is converted to float using float(). We then calculate the value of y using the equation y = x ** 2 + 6 * x + 9. The calculated value is stored in the variable y. Finally, we display the calculated value of y.


## Exercise 12: Find the length of 'python' and 'dragon' and make a falsy comparison statement

word1 = 'python'
word2 = 'dragon'
length1 = len(word1)
length2 = len(word2)
comparison = length1 == length2
print("The length of 'python' is", length1)
print("The length of 'dragon' is", length2)
print("The comparison statement is", comparison)

Here, we have two variables word1 and word2, storing the strings 'python' and 'dragon', respectively. We calculate the length of each string using the len() function and store the results in the variables length1 and length2. We then compare the lengths using the == operator and store the result in the variable comparison. Finally, we display the lengths of the strings and the comparison statement.


## Exercise 13: Use the `and` operator to check if 'on' is found in both 'python' and 'dragon'

word1 = 'python'
word2 = 'dragon'
check = 'on' in word1 and 'on' in word2
print("The 'on' is found in both 'python' and 'dragon':", check)

In this exercise, we check if the substring 'on' is present in both the strings 'python' and 'dragon'. We use the in operator and the and operator to perform the check. The result is stored in the variable check. Finally, we display whether 'on' is found in both strings or not.


## Exercise 14: Use the `in` operator to check if 'jargon' is in the sentence

sentence = "I hope this course is not full of jargon."
check = 'jargon' in sentence
print("The sentence contains 'jargon':", check)

Here, we have a sentence stored in the variable sentence. We check if the substring 'jargon' is present in the sentence using the in operator. The result is stored in the variable check. Finally, we display whether the sentence contains 'jargon' or not.


## Exercise 15: Check if 'on' is not present in both 'dragon' and 'python'

word1 = 'python'
word2 = 'dragon'
check = 'on' not in word1 and 'on' not in word2
print("There is no 'on' in both 'dragon' and 'python':", check)

In this exercise, we check if the substring 'on' is not present in both the strings 'python' and 'dragon'. We use the not in operator and the and operator to perform the check. The result is stored in the variable check. Finally, we display whether 'on' is not found in both strings or not.


## Exercise 16: Find the length of the text 'python' and convert it to a float and then to a string

text = 'python'
length = len(text)
length_float = float(length)
length_str = str(length_float)
print("The length of 'python' is", length_str)

Here, we have a string 'python' stored in the variable text. We calculate the length of the string using the len() function and store it in the variable length. We then convert the length to a float using float() and store it in the variable length_float. Finally, we convert the float value back to a string using str() and store it in the variable length_str. We display the length of 'python' as a string.


## Exercise 17: Check if a number is even or odd

number = int(input("Enter a number: "))
if number % 2 == 0:
    print(number, "is an even number.")
else:
    print(number, "is an odd number.")

In this exercise, we ask the user to enter a number. The input is converted to an integer using int(). We then use the modulus operator % to check if the number is divisible by 2. If the remainder is 0, we print that the number is even. Otherwise, we print that the number is odd.




