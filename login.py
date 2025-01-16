
#this file is used for asking if the user wants to input their own password or have a generated one done automatically
#Aref Turkieh



from password import *
from generate import *


def process_password(min_strength):
    while True:
        user_input = input("Type in a new password or type X or x for a randomly generated password: ")
        if user_input.lower() == "x": #if the user inputs X or x a random password would be generated
            generated_password = generate_password(15) #with a length of 15
            password_strength_value = password_strength(generated_password)

            print(f"Your generated password is:{generated_password}") #this would give us the generated password
            print(f"Your password strength is: {password_strength_value}") #this would give us its strength

            if password_strength_value < min_strength:
                print("Your password is not strong enough. Try again.") #if the password strength is < min strength then we have to try again
            else: # if password strength >= min strength then loop breaks
                print("Your password is strong enough.")
                break

        else:
            password_strength_value = password_strength(user_input)
            print(f"Your entered password is: {user_input}") # user inputs their own password
            print(f"Your password strength is: {password_strength_value}")
            if password_strength_value < min_strength:
                print("Your password is not strong enough. Try again.")
            else:
                print("Your password is strong enough.")
                break #loop breaks
if __name__ == "__main__":
    process_password(3) #password has to have a minimum strength of 3 for it to be complete




