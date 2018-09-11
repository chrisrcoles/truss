import unittest
from io import StringIO
from unittest import mock
from unittest.mock import patch

from csvparser import write_to_stdout, create_string, write_body, write_header, write_to_file, write_new_line


class ParserTest(unittest.TestCase):

    def test_write_to_stdout(self):
        args = 'Hello World'
        out = StringIO()
        write_to_stdout(args, out=out)
        output = out.getvalue().strip()
        self.assertEqual(output, args)


    def test_create_string(self):
        csv_byte_string = b'This is some Unicode right h\xffxxx \xc3\xbc \xc2\xa1! \xf0\x9f\x98\x80\n2/29/16 12:11:11 PM,111 Ste. #123123123,1101,R\xc3\xa9sum\xc3\xa9 Ron,31:23:32.123,1:32:33.123,zzsasdfa,\xf0\x9f\x8f\xb3\xef\xb8\x8f\xf0\x9f\x8f\xb4\xf0\x9f\x8f\xb3\xef\xb8\x8f\xf0\x9f\x8f\xb4\n1/1/11 12:00:01 AM'
        csv_string = 'This is some Unicode right h�xxx ü ¡! 😀\n2/29/16 12:11:11 PM,111 Ste. #123123123,1101,Résumé Ron,31:23:32.123,1:32:33.123,zzsasdfa,🏳️🏴🏳️🏴\n1/1/11 12:00:01 AM'
        self.assertEqual(create_string(csv_byte_string), csv_string)


    @patch('csvparser.parser.write_to_file')
    @patch('csvparser.parser.write_new_line')
    def test_write_body(self, write_new_line_mock, write_to_file_mock):
        write_body('foo', 'bar', 'timestamp', 'address', 'zipcode', 'name', 'total_duration', 'notes')
        self.assertTrue(write_to_file_mock.called)
        self.assertEqual(write_to_file_mock.call_count, 8)
        self.assertTrue(write_new_line_mock.called)
        self.assertEqual(write_new_line_mock.call_count, 1)


    @patch('csvparser.parser.write_to_file')
    @patch('csvparser.parser.write_new_line')
    def test_write_header(self, write_new_line_mock, write_to_file_mock):
        headers = ['Timestamp', 'Address', 'ZIP', 'FullName', 'FooDuration', 'BarDuration', 'TotalDuration', 'Notes']
        write_header(headers)
        self.assertTrue(write_to_file_mock.called)
        self.assertEqual(write_to_file_mock.call_count, len(headers))
        self.assertTrue(write_new_line_mock.called)
        self.assertEqual(write_new_line_mock.call_count, 1)


    def test_write_to_file(self):
        with mock.patch('csvparser.parser.write_to_stdout', autospec=True) as mock_write_to_stdout:
            val = 'Hello World'
            write_to_file(val, delimiter=',')
            mock_write_to_stdout.assert_called_once_with('{}{}'.format(val, ','))


    def test_write_new_line(self):
        with mock.patch('csvparser.parser.write_to_stdout', autospec=True) as mock_write_to_stdout:
            write_new_line()
            mock_write_to_stdout.assert_called_once_with('\n')