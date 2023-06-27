import re

# Exercise: Level 1

# 1. Find the most frequent word in the paragraph

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

# Split the paragraph into words
words = re.findall(r'\b\w+\b', paragraph)

# Count the occurrences of each word
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# Find the most frequent word
most_frequent_word = max(word_counts, key=word_counts.get)

print("Most frequent word:", most_frequent_word)

# 2. Find the distance between the two furthest particles

points = ['-1', '2', '-4', '-3', '-1', '0', '4', '8']
sorted_points = sorted(map(int, points))
distance = sorted_points[-1] - sorted_points[0]

print("Distance between furthest particles:", distance)

# Exercise: Level 2

# 1. Check if a string is a valid Python variable

def is_valid_variable(variable):
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    match = re.match(pattern, variable)
    return bool(match)

# Test the function with example inputs
print("Is 'first_name' a valid variable?", is_valid_variable('first_name'))
print("Is 'first-name' a valid variable?", is_valid_variable('first-name'))
print("Is '1first_name' a valid variable?", is_valid_variable('1first_name'))
print("Is 'firstname' a valid variable?", is_valid_variable('firstname'))

# Exercise: Level 3

# Clean the text and count the three most frequent words

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

def clean_text(text):
    # Remove special characters and symbols
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text)

    # Convert to lowercase
    cleaned_text = cleaned_text.lower()

    return cleaned_text

def most_frequent_words(text, n=3):
    words = text.split()
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:n]

cleaned_text = clean_text(sentence)
frequent_words = most_frequent_words(cleaned_text)

print("Three most frequent words:", frequent_words)
