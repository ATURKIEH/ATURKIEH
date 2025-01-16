
#this file is used to evaluate a password given by the user depending on the length and the different groups that are in it
#Aref Turkieh

import string
#the different groups that allow us to get the password strength
LOWERCASE = set(string.ascii_lowercase)
UPPERCASE = set(string.ascii_uppercase)
DIGITS = set(string.digits)
PUNCTUATION = set("!@#$%^&*/?-+=,.|~") #special characters

def count_groups(pwd):
   groups_used = set()

   for char in pwd:
    if char in LOWERCASE:
        groups_used.add("lowercase")
    if char in UPPERCASE:
        groups_used.add("uppercase")
    if char in DIGITS:
        groups_used.add("digits")
    if char in PUNCTUATION:
        groups_used.add("punctuation")

   return len(groups_used)

def password_strength(pwd): #function that gives the password strength depending on the length and the amount of groups in the password
    if any(char in ' \t\n' for char in pwd): #if \t or \n or space are in password then the password strength is 0
        return 0
    groups_count = count_groups(pwd)

    # Determine password length
    length = len(pwd)

    # Calculate strength based on the given rules
    if length < 5:
        return 0
    elif length >= 5 and length <= 8 and 0 <= groups_count <= 1:
        return 1
    elif length >= 5 and length <= 8 and 2 <= groups_count <= 3:
        return 2
    elif length >= 5 and length <= 8 and groups_count == 4:
        return 3
    elif length >= 9 and length <= 12 and 0 <= groups_count <= 1:
        return 2
    elif length >= 9 and length <= 12 and 2 <= groups_count <= 3:
        return 3
    elif length >= 9 and length <= 12 and groups_count == 4:
        return 4
    elif length > 12 and 0 <= groups_count <= 1:
        return 3
    elif length > 12 and 2 <= groups_count <= 3:
        return 4
    elif length > 12 and groups_count == 4:
        return 5
    else:
        return 0

if __name__ == '__main__':
    print(password_strength('<PASSWORD>'))
    print(password_strength('abc123'))
