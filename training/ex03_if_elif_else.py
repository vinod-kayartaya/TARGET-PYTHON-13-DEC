"""
We can check different related conditions using the if-elif-else statements
"""


def calculate_simple_interest(principal, term) -> str:
    if term < 1:
        raise ValueError('term/duration must be >= 1')
    elif term <= 3:
        roi = 3.5
    elif term <= 12:
        roi = 4.0
    elif term <= 24:
        roi = 6.5
    elif term <= 36:
        roi = 7.1
    elif term <= 60:
        roi = 6.8
    else:
        roi = 6.0

    return principal * roi * term / 100


def main():
    loan_amount = int(input('Enter the loan amount: '))
    no_of_months = int(input('Enter the number of months: '))

    interest_amount = calculate_simple_interest(loan_amount, no_of_months)
    print(f'interest amount for the given loan amount and duration is {interest_amount}')


main()
