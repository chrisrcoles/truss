import unittest

from csvparser import get_duration_over_24_hours, localize_timezone, parse_date, get_time, CustomTime, parse_time


class UtilsHelpersTest(unittest.TestCase):


    def test_get_duration_over_24_hours(self):
        self.assertEqual(get_duration_over_24_hours(['4 day', ' 0:23:02.000000']), '96:23:02.000000')
        self.assertEqual(get_duration_over_24_hours(['1 day', ' 8:56:05.246000']), '32:56:05.246000')
        self.assertEqual(get_duration_over_24_hours(['2 day', ' 0:00:00.000000']), '48:00:00.000000')


    def test_localize_timezone(self):
        self.assertEqual(localize_timezone(parse_date('2012-10-05 22:31:11'), 'US/Pacific', 'US/Eastern'),
                         parse_date('2012-10-06 01:31:11-04:00'))
        self.assertEqual(localize_timezone(parse_date('2004-10-02 08:44:11'), 'US/Eastern', 'US/Pacific'),
                         parse_date('2004-10-02 05:44:11-07:00'))
        self.assertEqual(localize_timezone(parse_date('2013-12-25 08:44:11'), 'US/Eastern', 'US/Mountain'),
                          parse_date('2013-12-25 06:44:11-07:00'))


    def test_get_time_custom_time(self):
        time = '31:23:32.123000'
        time_split = time.split(':')
        custom_time_1 = CustomTime(hour=int(time_split[0]), minute=int(time_split[1]),
                          second=int(time_split[2].split('.')[0]),
                          microsecond=int(time_split[2].split('.')[1]))

        t_1 = get_time(time)
        self.assertEqual(t_1.hour, custom_time_1.hour)
        self.assertEqual(t_1.minute, custom_time_1.minute)
        self.assertEqual(t_1.second, custom_time_1.second)
        self.assertEqual(t_1.microsecond, custom_time_1.microsecond)


    def test_get_time(self):
        self.assertEqual(get_time('01:23:32.12300'), parse_time('01:23:32.12300'))
        self.assertEqual(get_time('11:42:02.10000'), parse_time('11:42:02.10000'))