import random
import string

# Define character pools for lowercase, uppercase, and numbers
lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase
numbers = string.digits

# Combine all characters into a single list
all_chars = list(lower_case + upper_case + numbers)

# Ask the user for the desired password length
length = int(input("Enter the length of the password: "))

# Generate random characters to form the password list
password_list = []
for i in range(length):
    password_list.append(random.choice(all_chars))

# Shuffle the password list randomly
random.shuffle(password_list)

# Convert the list into a final string
password = "".join(password_list)

print("Generated Password:", password)
