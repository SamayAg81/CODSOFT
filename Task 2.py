# TASK 2
# A password generator is a useful tool that generates strong and

# random passwords for users. This project aims to create a
# password generator application using Python, allowing users to

# specify the length and complexity of the password.

# User Input: Prompt the user to specify the desired length of the

# password.

# Generate Password: Use a combination of random characters to

# generate a password of the specified length.

# Display the Password: Print the generated password on the screen.



import random
import string

pass_len = int(input("Enter the length of the password you want:"))
charValues = string.ascii_letters + string.digits + string.punctuation

#list comprehension [function for i in range(n)]

res = "".join([random.choice(charValues) for i in range(pass_len)])

#password = ""
#for i in range(pass_len):
#    password += random.choice(charValues)

print("Your random password is:", res)
