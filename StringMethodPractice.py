# Validate user input exercise

#1. username is no more than 12 characters
#2. username must not contain spaces
#3. usernmae must not contain digits

username = input("Enter your username: ") 

username.isalpha( )

if len(username) > 12:
    print("User name cannot be more than 12 characters")
elif not username.find (" ") == -1:
    print("Your user name cannot contain spaces")
elif not username.isalpha ():
    print("Your username cannot contain digits")
else:
    print(f"Welcome {username}")

# These are useful string methods used for programming. There are plenty more.