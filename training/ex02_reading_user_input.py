"""
Example for handling user inputs

We can use the `input` built in method to read a string from the user. If you want to accept
a numerical value, then we may have to convert the accepted value into either `int` or `float`.
"""


user_name = input('What is your name? ')
user_age = input('How old are you? ')

if user_age.isdigit():
    user_age = int(user_age)  # constructing an int object using a str object
    print(f'Hello {user_name}, in another 10 years you will be {user_age+10} years old.')
else:
    print('Sorry, I don\'t understand the input for the age.')

print('Have a nice day.')
print('bye.')