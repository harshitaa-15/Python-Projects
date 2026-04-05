
import random
import time
import sys

user_name = input("Enter your name:")

WELCOME_ASCII = r"""
__        __   _                            _
\ \      / /__| | ___ ___  _ __ ___   ___  | |
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | |
  \ V  V /  __/ | (_| (_) | | | | | |  __/ |_|
   \_/\_/ \___|_|\___\___/|_| |_| |_|\___| (_)
"""
# typing effect on ASCII text
for line in WELCOME_ASCII.splitlines():
    print(line)
    time.sleep(0.07)

print("\n")

msg = f"Welcome {user_name}! Generate the Passwords !!!"
for char in msg:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.05)

print("\n")


#=======================================================================================================
#                                       Password Generator Code
#=======================================================================================================


while True:
    try:
        number_passwords = int(input("Enter Number of Password :"))
        break
    except ValueError:
        print("Please Enter a Integer Value.")

list_of_lengths_passwords = []

print("Please Enter the Passwords Length between 8 and 20. \n")
for i in range(number_passwords):
    while True:
        try:
            length_password = int(input(f"Enter Length of Passwords {i + 1} : "))
            if length_password >= 8 and length_password <= 20:
                list_of_lengths_passwords.append(length_password)
                break
            else:
                print("Please Enter between 8 and 20")
        except ValueError:
            print("Please Enter a Integer Value. ")

list_chars = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',"0", "1", "2", "3", "4", "5", "6", "7", "8", "9","!", "@", "#", "$", "&", "*", "=", "?", ".", ","
]

random.shuffle(list_chars)
i = 1

print("#====================================================================================#")
print("#                                  YOUR PASSWORDS                                    #")
print("#====================================================================================#")

for length in list_of_lengths_passwords:
    print(f" Password {i} : {''.join(random.sample(list_chars, length))}")
    i = i + 1
    time.sleep(0.1)
