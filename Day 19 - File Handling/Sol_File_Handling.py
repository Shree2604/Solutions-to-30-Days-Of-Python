import json
import re
from collections import Counter

# Exercise: Level 1

def count_lines_and_words(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        num_lines = len(lines)

        words = re.findall(r'\b\w+\b', ' '.join(lines))
        num_words = len(words)

    return num_lines, num_words

# a) Read obama_speech.txt file and count number of lines and words
obama_lines, obama_words = count_lines_and_words('./data/obama_speech.txt')
print("Obama's speech:")
print("Number of lines:", obama_lines)
print("Number of words:", obama_words)
print()

# b) Read michelle_obama_speech.txt file and count number of lines and words
michelle_lines, michelle_words = count_lines_and_words('./data/michelle_obama_speech.txt')
print("Michelle Obama's speech:")
print("Number of lines:", michelle_lines)
print("Number of words:", michelle_words)
print()

# c) Read donald_speech.txt file and count number of lines and words
donald_lines, donald_words = count_lines_and_words('./data/donald_speech.txt')
print("Donald Trump's speech:")
print("Number of lines:", donald_lines)
print("Number of words:", donald_words)
print()

# d) Read melina_trump_speech.txt file and count number of lines and words
melina_lines, melina_words = count_lines_and_words('./data/melina_trump_speech.txt')
print("Melina Trump's speech:")
print("Number of lines:", melina_lines)
print("Number of words:", melina_words)
print()

# Exercise: Level 1

def most_spoken_languages(filename, n):
    with open(filename, 'r') as file:
        data = json.load(file)

        languages = Counter()
        for country in data:
            if 'languages' in country:
                languages.update(country['languages'])

        most_spoken = languages.most_common(n)

    return most_spoken

# Your output should look like this
print("Ten most spoken languages:")
print(most_spoken_languages(filename='./data/countries_data.json', n=10))
print()

# Your output should look like this
print("Three most spoken languages:")
print(most_spoken_languages(filename='./data/countries_data.json', n=3))
print()

# Exercise: Level 1

def most_populated_countries(filename, n):
    with open(filename, 'r') as file:
        data = json.load(file)

        sorted_countries = sorted(data, key=lambda x: x['population'], reverse=True)
        most_populated = sorted_countries[:n]

    return most_populated

# Your output should look like this
print("Ten most populated countries:")
print(most_populated_countries(filename='./data/countries_data.json', n=10))
print()

# Your output should look like this
print("Three most populated countries:")
print(most_populated_countries(filename='./data/countries_data.json', n=3))
print()

# Exercise: Level 2

def extract_email_addresses(filename):
    with open(filename, 'r') as file:
        text = file.read()
        email_addresses = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)

    return email_addresses

# Extract all incoming email addresses as a list from the email_exchange_big.txt file
email_addresses = extract_email_addresses('./data/email_exchange_big.txt')
print("Email addresses:")
print(email_addresses)
print()

# Exercise: Level 2

def find_most_common_words(string_or_file, n):
    if isinstance(string_or_file, str):
        text = string_or_file
    else:
        with open(string_or_file, 'r') as file:
            text = file.read()

    words = re.findall(r'\b\w+\b', text)
    word_counts = Counter(words)
    most_common_words = word_counts.most_common(n)

    return most_common_words

# Find the most common words in the English language
print("Ten most common words:")
print(find_most_common_words('sample.txt', 10))
print()

print("Five most common words:")
print(find_most_common_words('sample.txt', 5))
print()

# Exercise: Level 2

def find_most_frequent_words(speech_file, n):
    with open(speech_file, 'r') as file:
        speech = file.read()

    words = re.findall(r'\b\w+\b', speech)
    word_counts = Counter(words)
    most_frequent_words = word_counts.most_common(n)

    return most_frequent_words

# a) The ten most frequent words used in Obama's speech
obama_frequent_words = find_most_frequent_words('./data/obama_speech.txt', 10)
print("Ten most frequent words in Obama's speech:")
print(obama_frequent_words)
print()

# b) The ten most frequent words used in Michelle's speech
michelle_frequent_words = find_most_frequent_words('./data/michelle_obama_speech.txt', 10)
print("Ten most frequent words in Michelle's speech:")
print(michelle_frequent_words)
print()

# c) The ten most frequent words used in Trump's speech
trump_frequent_words = find_most_frequent_words('./data/donald_speech.txt', 10)
print("Ten most frequent words in Trump's speech:")
print(trump_frequent_words)
print()

# d) The ten most frequent words used in Melina's speech
melina_frequent_words = find_most_frequent_words('./data/melina_trump_speech.txt', 10)
print("Ten most frequent words in Melina's speech:")
print(melina_frequent_words)
print()

# Exercise: Level 3

def clean_text(text):
    with open('./data/stop_words.txt', 'r') as file:
        stop_words = file.read().splitlines()

    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text)
    cleaned_text = cleaned_text.lower()
    cleaned_text = ' '.join(word for word in cleaned_text.split() if word not in stop_words)

    return cleaned_text

def remove_support_words(text):
    with open('./data/support_words.txt', 'r') as file:
        support_words = file.read().splitlines()

    words = re.findall(r'\b\w+\b', text)
    filtered_words = [word for word in words if word.lower() not in support_words]
    filtered_text = ' '.join(filtered_words)

    return filtered_text

def check_text_similarity(text1, text2):
    cleaned_text1 = clean_text(text1)
    cleaned_text2 = clean_text(text2)

    filtered_text1 = remove_support_words(cleaned_text1)
    filtered_text2 = remove_support_words(cleaned_text2)

    similarity_score = len(set(filtered_text1.split()) & set(filtered_text2.split())) / float(len(set(filtered_text1.split()) | set(filtered_text2.split())))

    return similarity_score

# Check the similarity between the transcripts of Michelle's and Melina's speech
with open('./data/michelle_obama_speech.txt', 'r') as file:
    michelle_speech = file.read()

with open('./data/melina_trump_speech.txt', 'r') as file:
    melina_speech = file.read()

similarity_score = check_text_similarity(michelle_speech, melina_speech)
print("Similarity between Michelle's and Melina's speech:")
print("Similarity Score:", similarity_score)
print()

# Exercise: Level 3

def find_most_repeated_words(filename, n):
    with open(filename, 'r') as file:
        text = file.read()

    words = re.findall(r'\b\w+\b', text)
    word_counts = Counter(words)
    most_repeated_words = word_counts.most_common(n)

    return most_repeated_words

# Find the 10 most repeated words in the romeo_and_juliet.txt
print("Ten most repeated words in Romeo and Juliet:")
print(find_most_repeated_words('./data/romeo_and_juliet.txt', 10))
print()

# Exercise: Level 3

def count_lines_with_keywords(filename, keywords):
    with open(filename, 'r') as file:
        lines = file.readlines()

    count = 0
    for line in lines:
        if any(keyword.lower() in line.lower() for keyword in keywords):
            count += 1

    return count

# a) Count the number of lines containing python or Python
python_count = count_lines_with_keywords('./data/hacker_news.csv', ['python', 'Python'])
print("Number of lines containing python or Python:", python_count)

# b) Count the number lines containing JavaScript, javascript or Javascript
javascript_count = count_lines_with_keywords('./data/hacker_news.csv', ['JavaScript', 'javascript', 'Javascript'])
print("Number of lines containing JavaScript, javascript or Javascript:", javascript_count)

# c) Count the number lines containing Java and not JavaScript
java_count = count_lines_with_keywords('./data/hacker_news.csv', ['Java'])
javascript_count = count_lines_with_keywords('./data/hacker_news.csv', ['JavaScript', 'javascript', 'Javascript'])
java_only_count = java_count - javascript_count
print("Number of lines containing Java and not JavaScript:", java_only_count)
