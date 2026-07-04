import random
import string

# Get password length from the user
length = int(input("Enter the desired password length: "))

# Characters to use in the password
characters = string.ascii_letters + string.digits + string.punctuation

# Generate the password
password = "".join(random.choice(characters) for _ in range(length))

print(f"\nGenerated Password:{password}")