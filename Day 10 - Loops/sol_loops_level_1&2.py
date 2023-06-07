
# Exercises: Level 1

# Iterate 0 to 10 using a for loop
for number in range(11):
    print(number)

# Iterate 0 to 10 using a while loop
number = 0
while number <= 10:
    print(number)
    number += 1

# Iterate 10 to 0 using a for loop
for number in range(10, -1, -1):
    print(number)

# Iterate 10 to 0 using a while loop
number = 10
while number >= 0:
    print(number)
    number -= 1

# Print a triangle using a loop
for i in range(1, 8):
    print("#" * i)

# Print a rectangular pattern using nested loops
for _ in range(8):
    for _ in range(8):
        print("#", end=" ")
    print()

# Print the multiplication table using a loop
for i in range(11):
    print(f"{i} x {i} = {i*i}")

# Iterate through a list and print its items
items = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for item in items:
    print(item)

# Print even numbers using a loop
for number in range(101):
    if number % 2 == 0:
        print(number)

# Print odd numbers using a loop
for number in range(101):
    if number % 2 != 0:
        print(number)

# Exercises: Level 2

# Calculate the sum of numbers from 0 to 100
total = 0
for number in range(101):
    total += number
print("The sum of all numbers is", total)

# Calculate the sum of even and odd numbers from 0 to 100
sum_even = 0
sum_odd = 0

for number in range(101):
    if number % 2 == 0:
        sum_even += number
    else:
        sum_odd += number

print("The sum of all evens is", sum_even)
print("The sum of all odds is", sum_odd)
