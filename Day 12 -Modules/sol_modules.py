import random
import string

# Exercise: Level 1

# Function to generate a six-digit random_user_id
def random_user_id():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(6))

print(random_user_id())

# Function to generate user-defined random_user_ids
def user_id_gen_by_user():
    num_chars = int(input('Enter the number of characters: '))
    num_ids = int(input('Enter the number of IDs to generate: '))
    characters = string.ascii_letters + string.digits
    ids = []
    for i in range(num_ids):
        id = ''.join(random.choice(characters) for i in range(num_chars))
        ids.append(id)
    return ids

print(user_id_gen_by_user())

# Function to generate random RGB colors
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f'rgb({r},{g},{b})'

print(rgb_color_gen())

# Exercise: Level 2

# Function to generate a list of hexadecimal colors
def list_of_hexa_colors(num_colors):
    hex_colors = []
    for _ in range(num_colors):
        hex_color = '#' + ''.join(random.choices('0123456789abcdef', k=6))
        hex_colors.append(hex_color)
    return hex_colors

print(list_of_hexa_colors(5))

# Function to generate a list of RGB colors
def list_of_rgb_colors(num_colors):
    rgb_colors = []
    for _ in range(num_colors):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        rgb_color = f'rgb({r},{g},{b})'
        rgb_colors.append(rgb_color)
    return rgb_colors

print(list_of_rgb_colors(5))

# Function to generate either hexa or rgb colors
def generate_colors(color_type, num_colors):
    colors = []
    if color_type == 'hexa':
        for _ in range(num_colors):
            hex_color = '#' + ''.join(random.choices('0123456789abcdef', k=6))
            colors.append(hex_color)
    elif color_type == 'rgb':
        for _ in range(num_colors):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            rgb_color = f'rgb({r},{g},{b})'
            colors.append(rgb_color)
    return colors

print(generate_colors('hexa', 3))
print(generate_colors('rgb', 3))

# Exercise: Level 3

# Function to shuffle a given list
def shuffle_list(lst):
    random.shuffle(lst)
    return lst

my_list = [1, 2, 3, 4, 5]
print(shuffle_list(my_list))

# Function to generate an array of seven unique random numbers in the range of 0-9
def generate_random_numbers():
    numbers = random.sample(range(10), 7)
    return numbers

print(generate_random_numbers())
