import time
import json
import threading


class CsvUtil(threading.Thread):
    def __init__(self, csv_file):
        super().__init__()
        self.csv_file = csv_file

    @staticmethod
    def to_dict(line1: str, line2: str, delim=',') -> dict:
        if type(line1) is not str or type(line2) is not str:
            raise ValueError('Invalid value supplied. Must be 2/3 strings')

        keys = [k.strip() for k in line1.strip().split(delim)]
        keys = [int(k) if k.isdigit() else k for k in keys]
        values = [v.strip() for v in line2.strip().split(delim)]
        values = [int(v) if v.isdigit() else v for v in values]
        return dict(zip(keys, values))

    def run(self):
        # assumption --> filename is just the filename without the path
        csv_filename = self.csv_file.name
        json_filename = f'{csv_filename[:-4]}_{time.time()}.json'
        header = self.csv_file.readline()
        data = [CsvUtil.to_dict(header, a_line) for a_line in self.csv_file]
        with open(json_filename, mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        print(f'{json_filename} is created successfully')


if __name__ == '__main__':
    csv_filename = input('Enter csv filename: ')
    with open(csv_filename) as csv_file:
        util = CsvUtil(csv_file)
        util.start()
        util.join()  # waits for util.run() to finish

    print('end of main thread')