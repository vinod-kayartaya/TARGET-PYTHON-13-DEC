"""
Using the `in` operator with `if` statements
"""

if __name__ == '__main__':
    user_name = input('Enter your name: ')
    user_gender = input('Enter your gender: ')

    msg = f'Hello {user_name}!'
    if user_gender.lower() in ('m', 'male'):
        msg = f'Hello Mr.{user_name}'
    elif user_gender.lower() in ('f', 'female'):
        msg = f'Hello Ms.{user_name}'

    print(msg)
