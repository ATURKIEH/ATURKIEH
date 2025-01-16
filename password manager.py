#master password
  #while true:
    #add a new password? yes or no
    #if yes
        #enter the password you would like to add. append

    #if no
        #view all passwords
    #else:
        #invalid answer, redo it
from cryptography.fernet import Fernet
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


def view():
    with open('password.txt', 'r') as f:
         for line in f.readlines():
             data = line.rstrip()
             user, passw = data.split('|')
             print(f"User: {user} | Password: {fer.decrypt(passw.encode()).decode()}")

def add():
    account = input("Account name: ")
    password = input("Password: ")

    with open("password.txt", "a") as f:
        f.write(f"{account} | {fer.encrypt(password.encode()).decode()}\n")


key = load_key()
fer = Fernet(key)
while True:
    mode = input("Would like to add a new password, or view all passwords?(view/add)(q to quit): ").strip()
    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    elif mode == 'q':
        break
    else:
        print("Invalid mode")
        continue


