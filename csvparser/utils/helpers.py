import datetime
from typing import Sequence, Union

import dateutil.parser
import pytz

Num = Union[int, float]


class CustomTime(object):
    def __init__(self, hour: int, minute: int, second: int, microsecond: int):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.microsecond = microsecond


def get_time(time: str) -> Union[CustomTime, datetime.time]:
    if not time:
        return parse_time('00:00:00.000000')
    try:
        return parse_time(time)
    except ValueError as e:
        # ValueError is raised when hour > 24
        time_split = time.split(':')
        return CustomTime(hour=int(time_split[0]), minute=int(time_split[1]),
                          second=int(time_split[2].split('.')[0]),
                          microsecond=int(time_split[2].split('.')[1]))


def get_time_delta(hour: int, minute: int, second: int, microsecond: int) -> datetime.timedelta:
    return datetime.timedelta(hours=hour, minutes=minute,
                            seconds=second, microseconds=microsecond)


def get_duration_over_24_hours(total: Sequence[str]) -> str:
    days = int(total[0].split(' ')[0])
    existing_time = [t.strip() for t in total[1].split(':')]

    existing_hours = int(existing_time[0])
    total_hours = (days * 24) + existing_hours
    existing_time.pop(0)
    existing_time.insert(0, str(total_hours))

    return (':').join(existing_time)


def localize_timezone(date: datetime.datetime, old_timezone: str, new_timezone) -> datetime.time:
    with_old_timezone = pytz.timezone(old_timezone)
    with_new_timezone = pytz.timezone(new_timezone)
    date_old_timezone = with_old_timezone.localize(date)
    return date_old_timezone.astimezone(with_new_timezone)


def parse_time(time: str) -> datetime.time:
    return datetime.datetime.strptime(time, '%H:%M:%S.%f').time()


def parse_date(date: str) -> datetime.datetime:
    return dateutil.parser.parse(date)