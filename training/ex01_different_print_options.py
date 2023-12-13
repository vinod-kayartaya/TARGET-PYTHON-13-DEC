"""
This is an example module to understand different printing styles.

There are 4 different ways to print values of variables
"""


my_name = 'Vinod'
my_age = 50
my_city = 'Bangalore'

print('My name is ', my_name, ' (', my_age, ' years) living in ', my_city, '.', sep='')
print('My name is %s (%d years) living in %s.' % (my_name, my_age, my_city))
print('My name is {} ({} years) living in {}.'.format(my_name, my_age, my_city))
print(f'My name is {my_name} ({my_age} years) living in {my_city}.')
