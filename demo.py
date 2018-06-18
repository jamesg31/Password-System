import passsys
import getpass
import os
import time

passsys.setup('data.db')

def login():
    os.system('cls' if os.name=='nt' else 'clear')
    print('You have the following options:')
    print('1. Login')
    print('2. Create New User')
    print('3. Quit')
    option = input('\nEnter the option number to select: ')
    if option == '1':
        username = input('Username: ')
        password = getpass.getpass('Password: ')
        check = passsys.checkUser(username, password)
        if check:
            print('Login Successful')
            time.sleep(3)
            os.system('cls' if os.name=='nt' else 'clear')
            login()
        else:
            print('Login Failed: Invalid Details')
            time.sleep(3)
            os.system('cls' if os.name=='nt' else 'clear')
            login()
    elif option == '2':
        newusername = input('New Username: ')
        newpassword = getpass.getpass('New Password: ')
        reenterpassword = getpass.getpass('Re-Enter Password: ')
        if newpassword == reenterpassword:
            passsys.createUser(newusername, newpassword)
            print('Account Creation Successful')
            time.sleep(3)
            os.system('cls' if os.name=='nt' else 'clear')
            login()
        else:
            print('Account Creation Failed: Passwords Not Matching')
            time.sleep(3)
            os.system('cls' if os.name=='nt' else 'clear')
            login()
    elif option == '3':
        passsys.save()
    else:
        print('Invalid Entry')
        time.sleep(3)
        os.system('cls' if os.name=='nt' else 'clear')
        login()

login()
