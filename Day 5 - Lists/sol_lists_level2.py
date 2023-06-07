# Exercise: Level 2

# Question 1: The following is a list of 10 students' ages
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Question 2: Sort the list and find the minimum and maximum age
ages.sort()
min_age = ages[0]
max_age = ages[-1]

# Question 3: Add the minimum age and the maximum age again to the list
ages.append(min_age)
ages.append(max_age)

# Question 4: Find the median age (one middle item or two middle items divided by two)
import statistics
median_age = statistics.median(ages)

# Question 5: Find the average age (sum of all items divided by their number)
average_age = sum(ages) / len(ages)

# Question 6: Find the range of the ages (maximum minus minimum)
range_of_ages = max_age - min_age

# Question 7: Compare the value of (min - average) and (max - average) using the abs() method
min_avg_diff = abs(min_age - average_age)
max_avg_diff = abs(max_age - average_age)

# Question 8: Find the middle country(ies) in the countries list
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
middle_country = countries[len(countries)//2]

# Question 9: Divide the countries list into two equal lists if it is even; if not, add one more country for the first half
first_half = countries[len(countries)//2 + len(countries)%2]
second_half = countries[len(countries)//2 + len(countries)%2:]

# Question 10: Unpack the first three countries and the rest as Scandic countries
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
china, russia, usa, *scandic_countries = countries

# Print the results
print("Minimum age:", min_age)
print("Maximum age:", max_age)
print("Median age:", median_age)
print("Average age:", average_age)
print("Range of ages:", range_of_ages)
print("Difference between min and average age:", min_avg_diff)
print("Difference between max and average age:", max_avg_diff)
print("Middle country:", middle_country)
print("First half of countries:", first_half)
print("Second half of countries:", second_half)
print("First three countries:", china, russia, usa)
print("Scandic countries:", scandic_countries)
