import unittest
from my_utils import to_dict


class TestingToDictMethod(unittest.TestCase):
    def test_basic_case(self):
        line1 = 'name,age, city'
        line2 = 'vinod, 50, bangalore'
        actual = to_dict(line1, line2)
        expected = dict(name='vinod', age=50, city='bangalore')
        self.assertEqual(expected, actual)

    def test_header_with_numbers(self):
        line1 = '1,2,3'
        line2 = 'vinod,50,bangalore'
        actual = to_dict(line1, line2)
        expected = {1: 'vinod', 2: 50, 3: 'bangalore'}
        self.assertEqual(expected, actual)

    def test_with_mixed_types_in_header(self):
        line1 = 'id, name, 3, 4'
        line2 = '1122, Ramesh, ADMIN, 45000'
        actual = to_dict(line1, line2)
        expected = {'id': 1122, 'name': 'Ramesh', 3: 'ADMIN', 4: 45000}
        self.assertEqual(expected, actual)

    def test_with_different_delimiter(self):
        line1 = 'id; name; 3; 4'
        line2 = '1122; Ramesh; ADMIN; 45000'
        actual = to_dict(line1, line2, ';')
        expected = {'id': 1122, 'name': 'Ramesh', 3: 'ADMIN', 4: 45000}
        self.assertEqual(expected, actual)

    def test_with_numbers(self):
        with self.assertRaises(ValueError):
            to_dict(100, 200)


if __name__ == '__main__':
    unittest.main()
