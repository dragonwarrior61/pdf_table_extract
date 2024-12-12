import random
import string

def generate_random_string():
    letters = string.ascii_lowercase
    
    random_string = ''
    for i in range(4):
        random_string = random_string + random.choice(letters)
    return random_string

for i in range(5):
    print(generate_random_string())