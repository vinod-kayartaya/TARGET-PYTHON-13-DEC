from my_utils import csv2json

if __name__ == '__main__':
    input_filename = 'data_files/customers.csv'
    output_filename = csv2json(input_filename)
    if output_filename is not None:
        print(f'data written to "{output_filename}"')
    