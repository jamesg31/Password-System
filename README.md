# Password System
Thanks for checking out Password System. This will run you through all you need to get started with a full login system for your application. Please read the complete README so that you understand how to use the library.

## Downloading / Installing:
You can either download Password System through Github directly at https://github.com/jamesg31/Password-System or using `python -m pip install password-system`

Then import using `import password_system as passsys`

## Setup:

To setup you use the `passsys.setup(Data File)`

**Please Note: You need to create that file for the password system to work!**

## Adding Users:
Add a username and password with `passsys.addUser(username, password)` replacing username and password with the username and password variables.

Example:

    username = input("Username: ")
    password = input("Password: ")
    passsys.addUser(username, password)

## Checking Users:
To check a username and password against the database use the `passsys.checkUser(username, password)` which will return either *True* or *False* depending on whether the details matched details in the database.

Example:

    username = input("Username: ")
    password = input("Password: ")
    if passsys.checkUser(username, password) == True:
	    print("Login Successful")
	else:
		print("Login Unsuccessful")

## Saving:
At the end of your script, or when you complete the login process in the script, use the `passsys.save()` command to save all the changes to the database.

## Complete Example:
You can view a complete example of the Password Systems implementation at https://github.com/jamesg31/Password-System/blob/master/demo.py

## Support:
If you have any problems, please report it by making a new issue at https://github.com/jamesg31/Password-System/issues Please ensure you have read the complete README before creating a issue as your problem may be solved here.
