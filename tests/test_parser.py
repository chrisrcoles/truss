import unittest

from csvparser import create_string


class ParserTest(unittest.TestCase):


    def test_create_string(self):
        csv_byte_string = b'This is some Unicode right h\xffxxx \xc3\xbc \xc2\xa1! \xf0\x9f\x98\x80\n2/29/16 12:11:11 PM,111 Ste. #123123123,1101,R\xc3\xa9sum\xc3\xa9 Ron,31:23:32.123,1:32:33.123,zzsasdfa,\xf0\x9f\x8f\xb3\xef\xb8\x8f\xf0\x9f\x8f\xb4\xf0\x9f\x8f\xb3\xef\xb8\x8f\xf0\x9f\x8f\xb4\n1/1/11 12:00:01 AM'
        csv_string = 'This is some Unicode right h�xxx ü ¡! 😀\n2/29/16 12:11:11 PM,111 Ste. #123123123,1101,Résumé Ron,31:23:32.123,1:32:33.123,zzsasdfa,🏳️🏴🏳️🏴\n1/1/11 12:00:01 AM'
        self.assertEqual(create_string(csv_byte_string), csv_string)

