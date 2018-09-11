import unittest

from csvparser import normalize_duration, normalize_timestamp, normalize_address, normalize_zipcode, \
    normalize_name, normalize_total_duration, normalize_notes


class NormalizersTest(unittest.TestCase):


    def test_normalize_duration(self):
        self.assertEqual(normalize_duration('01:01:10.', 'foo'), '01:01:10.000000')
        self.assertEqual(normalize_duration('111:23:32.123', 'bar'), '111:23:32.123000')
        self.assertEqual(normalize_duration('01:23:32.123', 'foo'), '01:23:32.123000')
        self.assertEqual(normalize_duration('', 'foo'), '')
        self.assertEqual(normalize_duration('some text', 'bar'), '')


    def test_normalize_timestamp(self):
        self.assertEqual(normalize_timestamp('4/1/11 11:00:00 AM'), '2011-04-01T14:00:00-04:00')
        self.assertEqual(normalize_timestamp('12/31/16 11:59:59 PM'), '2017-01-01T02:59:59-05:00')
        self.assertEqual(normalize_timestamp(''), '')
        self.assertEqual(normalize_timestamp('some gibberish'), '')


    def test_normalize_address(self):
        self.assertEqual(normalize_address(''), '')
        self.assertEqual(normalize_address('123 4th St, Anywhere, AA'), '123 4th St, Anywhere, AA')
        self.assertEqual(normalize_address('This Is Not An Address, BusyTown, BT'), 'This Is Not An Address, BusyTown, BT')


    def test_normalize_zipcode(self):
        self.assertEqual(normalize_zipcode('94121'), '94121')
        self.assertEqual(normalize_zipcode('121'), '00121')
        self.assertEqual(normalize_zipcode('4'), '00004')
        self.assertEqual(normalize_zipcode(''), '00000')


    def test_normalize_name(self):
        self.assertEqual(normalize_name('Monkey Alberto'), 'MONKEY ALBERTO')
        self.assertEqual(normalize_name(''), '')
        self.assertEqual(normalize_name('Superman übertan'), 'SUPERMAN ÜBERTAN')
        self.assertEqual(normalize_name('株式会社スタジオジブリ'), '株式会社スタジオジブリ')


    def test_normalize_total_duration(self):
        self.assertEqual(normalize_total_duration('01:23:32.123000', '01:32:33.123000'), '2:56:05.246000')
        self.assertEqual(normalize_total_duration('200:23:32.123000', '0:00:00.000'), '200:23:32.123000')
        self.assertEqual(normalize_total_duration('01:23:32.123000', '01:32:33.123000'), '2:56:05.246000')
        self.assertEqual(normalize_total_duration('01:23:32.123000', ''), '1:23:32.123000')
        self.assertEqual(normalize_total_duration('', ''), '')


    def test_normalize_notes_with_unicode(self):
        self.assertEqual(normalize_notes('This is some Unicode right h�xxx ü ¡! 😀'), 'This is some Unicode right h�xxx ü ¡! 😀')
        self.assertEqual(normalize_notes('1:11:11.123'), '1:11:11.123')
        self.assertEqual(normalize_notes(''), '')
