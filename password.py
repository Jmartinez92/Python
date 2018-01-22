while True:
    firstname=input('What is your name?')

    if not(firstname.replace(' ','').isalpha()):

        print('Please enter letters only.')
    else:
        print('Hello ' + firstname + '!')

        break



import re

while True:
    password = input("Enter a password: ")

    length = len(password)
    if length < 8:
        print("Make sure your password is at least 8 letters")
    elif not re.search("[0-9]",password):
        print("Make sure your password has a number in it")
    elif not re.search('[A-Z]',password):
        print("Make sure your password has a capital letter in it.")
    elif not re.search('[a-z]',password):
        print("Make sure your password has a lower case in it.")
    elif not re.search(r'.*[\%\$^\*\@\!\_\-\(\)\:\;\'\"\{\}\[\]].*', password):
        print("Make sure to print a special character.")
    else:
        print("Your password seems fine")
        break
