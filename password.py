import secrets
import string

# Parola uzunluğu
length = secrets.choice(range(15, 25))

# Harfler, sayılar ve özel karakterler
symbols = string.ascii_letters \
    + string.digits \
    + string.punctuation
# Parola oluşturuluyor
password = "".join(secrets.choice(symbols)
                   for i in range(length))

print(password)

