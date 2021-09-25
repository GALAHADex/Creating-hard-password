import secrets
import string

# Password length
length = secrets.choice(range(15, 25))

# Letters, numbers and special characters
symbols = string.ascii_letters \
    + string.digits \
    + string.punctuation
# Generating password...
password = "".join(secrets.choice(symbols)
                   for i in range(length))

print(password)

