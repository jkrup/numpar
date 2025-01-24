import unittest
from numpar import parse_number

class TestNumberParser(unittest.TestCase):
    def test_basic_numbers(self):
        self.assertEqual(parse_number('123'), 123.0)
        self.assertEqual(parse_number('123.45'), 123.45)
        self.assertEqual(parse_number('-123.45'), -123.45)
        self.assertEqual(parse_number('+123.45'), 123.45)

    def test_comma_separators(self):
        self.assertEqual(parse_number('1,234'), 1234.0)
        self.assertEqual(parse_number('1,234,567'), 1234567.0)
        self.assertEqual(parse_number('1,234.56'), 1234.56)
        self.assertEqual(parse_number('1,234,567.89'), 1234567.89)

    def test_percentages(self):
        self.assertEqual(parse_number('50%'), 0.5)
        self.assertEqual(parse_number('100%'), 1.0)
        self.assertEqual(parse_number('12.34%'), 0.1234)
        self.assertEqual(parse_number('0.5%'), 0.005)

    def test_magnitude_suffixes(self):
        self.assertEqual(parse_number('1k'), 1000.0)
        self.assertEqual(parse_number('1.5k'), 1500.0)
        self.assertEqual(parse_number('1M'), 1000000.0)
        self.assertEqual(parse_number('2.5m'), 2500000.0)
        self.assertEqual(parse_number('1b'), 1000000000.0)
        self.assertEqual(parse_number('1.5B'), 1500000000.0)

    def test_whitespace(self):
        self.assertEqual(parse_number(' 123 '), 123.0)
        self.assertEqual(parse_number('\t123.45\n'), 123.45)
        self.assertEqual(parse_number('  1,234  '), 1234.0)
        self.assertEqual(parse_number(' 50% '), 0.5)

    def test_combined_formats(self):
        self.assertEqual(parse_number('1,234k'), 1234000.0)
        self.assertEqual(parse_number('1.5M'), 1500000.0)
        self.assertEqual(parse_number(' 1,234.56m '), 1234560000.0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            parse_number(123)
        with self.assertRaises(ValueError):
            parse_number('')
        with self.assertRaises(ValueError):
            parse_number('abc')
        with self.assertRaises(ValueError):
            parse_number('12.34.56')

if __name__ == '__main__':
    unittest.main()