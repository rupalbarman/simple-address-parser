import unittest

from address_parser.parser import parse

BASIC_CASES = [
    ('Winterallee 3', ('3', 'Winterallee')),
    ('Musterstrasse 45', ('45', 'Musterstrasse')),
    ('Blaufeldweg 123B', ('123B', 'Blaufeldweg')),
    ('Am Bächle 23', ('23', 'Am Bächle')),
    ('Auf der Vogelwiese 23 b', ('23 b', 'Auf der Vogelwiese')),
    ('4, rue de la revolution', ('4', 'rue de la revolution')),
    ('200 Broadway Av', ('200', 'Broadway Av')),
    ('Calle Aduana, 29', ('29', 'Calle Aduana')),
    ('Calle 39 No 1540', ('No 1540', 'Calle 39')),
]

EXTENDED_CASES = [
    ('some street 6', ('6', 'some street')),
    ('that street 10a', ('10a', 'that street')),
    ('your street 10 v', ('10 v', 'your street')),
    ('102 main street', ('102', 'main street')),
]

HARD_CASES = [
    ('building no 23113 south hampton street',
     ('building no 23113', 'south hampton street')),

    ('west ward avenue building 90', ('building 90', 'west ward avenue')),
    ('south block 34 kama road', ('block 34', 'south kama road')),  # fix
    ('kino moshita 90 98b', ('90 98b', 'kino moshita')),  # fix
]

OBSCURE_CASES = [
    ('829 LKSDFJlkjsdflkjsdljf Bkpw 12345',
     ('12345', '829 LKSDFJlkjsdflkjsdljf Bkpw')),  # fix

    ('205 1105 14 90210', ('1105 90210', '205 14')),
]


class TestParse(unittest.TestCase):
    def setUp(self):
        pass

    def test_basic_cases(self):
        for original, expected in BASIC_CASES:
            house, street = parse(original)
            self.assertEqual(house, expected[0], 'house does not match')
            self.assertEqual(street, expected[1], 'street does not match')

    def test_extended_cases(self):
        for original, expected in EXTENDED_CASES:
            house, street = parse(original)
            self.assertEqual(house, expected[0], 'house does not match')
            self.assertEqual(street, expected[1], 'street does not match')

    def test_hard_cases(self):
        for original, expected in HARD_CASES:
            house, street = parse(original)
            self.assertEqual(house, expected[0], 'house does not match')
            self.assertEqual(street, expected[1], 'street does not match')

    def test_obscure_cases(self):
        for original, expected in OBSCURE_CASES:
            house, street = parse(original)
            self.assertEqual(house, expected[0], 'house does not match')
            self.assertEqual(street, expected[1], 'street does not match')
