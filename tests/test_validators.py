import unittest

from csvparser import valid_duration


class ValidatorsTest(unittest.TestCase):

    def test_valid_duration(self):
        self.assertEqual(valid_duration('111:23:32.123'), True)
        self.assertEqual(valid_duration('01:23:32.123'), True)
        self.assertEqual(valid_duration(''), False)
        self.assertEqual(valid_duration('1000:00:00.000'), True)
        self.assertEqual(valid_duration('1000:0:0.000'), False)