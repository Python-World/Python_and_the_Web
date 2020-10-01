# importing modules
import random
import string

def get_random_password_string(length):
    password_characters = string.ascii_letters + string.digits + string.punctuation #taking randomg lett digits

    password = "".join(random.choice(password_characters) for i in range(length))
    print("Your Password is:", password)

passlen = int(input("**Secure Password Generator** \nEnter Password Length (Type in Digit) - ")) #asking user for length
   
get_random_password_string(passlen)