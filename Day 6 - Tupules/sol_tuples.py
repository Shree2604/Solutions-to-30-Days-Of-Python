# Exercises: Level 1

# Question 1: Create an empty tuple
my_tuple = ()

# Question 2: Create a tuple containing names of your sisters and your brothers
brothers = ('Venkky', 'Pranav')
sisters = ('Janu', 'Devi')

# Question 3: Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters

# Question 4: How many siblings do you have?
num_siblings = len(siblings)

# Question 5: Modify the siblings tuple and add the name of your father and mother
family_members = siblings + ('Dad', 'Mom')

# Exercises: Level 2

# Question 6: Unpack siblings and parents from family_members
*my_siblings, father, mother = family_members

# Question 7: Create fruits, vegetables, and animal products tuples. Join the three tuples and assign it to food_stuff_tp.
fruits = ('apple', 'banana', 'orange')
vegetables = ('carrot', 'potato', 'oninons')
animal_products = ('milk', 'eggs', 'cheese')
food_stuff_tp = fruits + vegetables + animal_products

# Question 8: Change the food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

# Question 9: Slice out the middle item from the food_stuff_tp tuple or food_stuff_lt list
middle_item_tp = food_stuff_tp[len(food_stuff_tp)//2]
middle_item_lt = food_stuff_lt[len(food_stuff_lt)//2]

# Question 10: Slice out the first three items and the last three items from the food_stuff_lt list
first_three_items = food_stuff_lt[:3]
last_three_items = food_stuff_lt[-3:]

# Question 11: Delete the food_stuff_tp tuple completely
del food_stuff_tp

# Check if an item exists in a tuple
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
'estonia' in nordic_countries # Returns False if Estonia is not in the tuple.
'iceland' in nordic_countries # Returns True if Iceland is in the tuple.
