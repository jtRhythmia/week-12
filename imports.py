import string
import random

lower_alphabet = string.ascii_lowercase
upper_alphabet = string.ascii_uppercase

password = ''

i = 1
while i < 13:
    # Get a random letter from the alphabet
    random_letter = random.choice(string.ascii_lowercase)

    # Add that random letter to my password
    password += random_letter

    i += 1

print(password)

