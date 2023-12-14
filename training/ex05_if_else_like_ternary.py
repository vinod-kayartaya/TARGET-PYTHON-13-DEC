if __name__ == '__main__':
    # following code will be run only when running this script directly by the python interpeter
    num = int(input('Enter a number: '))
    result = 'even' if num % 2 == 0 else 'odd'
    print(f'the given number {num} is an {result} number.')
