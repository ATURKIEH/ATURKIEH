import random
import string

ALL_CHARS = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

#this file is used to generate a random password with some guidelines that it should be at least 4 characters
#Aref Turkieh


def generate_password(length):
    if length < 4:
        raise ValueError("Password length must be at least 4 characters") #password has to have a length of at least 4

    password = [
        random.choice(ALL_CHARS)
    ] #password is made from all characters from the 4 different groups


    for _ in range(length-4):
        password.append(random.choice(ALL_CHARS))

    random.shuffle(password) #random order

    return ''.join(password)


if __name__ == "__main__":
    print(generate_password(10))
    print(generate_password(15))





