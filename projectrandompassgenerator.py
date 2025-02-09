import random
import string
passValues = string.ascii_letters + string.digits + string.punctuation

pass_len = 12
password = ""
for i in range(pass_len):
    password += random.choice(passValues)

print("Your Password is :", password)