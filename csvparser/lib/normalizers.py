import datetime
from typing import Union

from csvparser.utils import get_time, get_time_delta, get_duration_over_24_hours, parse_time, parse_date, localize_timezone
from .exceptions import ExceptionsManager, NException, NEXCEPTION
from .validators import valid_duration, valid, valid_timestamp

exceptions_manager = ExceptionsManager.getInstance()


def normalize_duration(time: str, type: str) -> str:
    if valid_duration(time):
        TOTAL_FLOATING_POINTS = 6

        try:
            normalized_time = str(parse_time(time))

            if '.' in normalized_time:
                return normalized_time
            else:
                return normalized_time + '.000000'
        except ValueError as e:
            milleseconds = time.split('.')[1]
            suffix = (TOTAL_FLOATING_POINTS - len(milleseconds)) * '0'
            return time + suffix
    else:
        if type == 'foo':
            return exceptions_manager.handle_exception(NException(attr=NEXCEPTION.FOO_DURATION, val=time))

        if type == 'bar':
            return exceptions_manager.handle_exception(NException(attr=NEXCEPTION.BAR_DURATION, val=time))


def normalize_total_duration(foo: str, bar: str) -> str:
    foo_valid = valid_duration(foo)
    bar_valid = valid_duration(bar)

    if foo_valid or bar_valid:
        foo_time = get_time(foo)
        bar_time = get_time(bar)

        foo_time_timedelta = get_time_delta(foo_time.hour, foo_time.minute, foo_time.second, foo_time.microsecond)
        bar_time_timedelta = get_time_delta(bar_time.hour, bar_time.minute, bar_time.second, bar_time.microsecond)

        total_timedelta = foo_time_timedelta + bar_time_timedelta
        total_split = str(total_timedelta).split(',')

        if len(total_split) == 1:
            return str(total_timedelta)
        elif len(total_split) == 2:
            return get_duration_over_24_hours(total_split)
    else:
        if not foo_valid:
            return exceptions_manager.handle_exception(NException(attr=NEXCEPTION.TOTAL_DURATION, val=foo))

        if not bar_valid:
            return exceptions_manager.handle_exception(NException(attr=NEXCEPTION.TOTAL_DURATION, val=bar))


def normalize_address(address: str) -> str:
    if valid(address):
        return address
    else:
        return exceptions_manager.handle_exception(NException(attr=NEXCEPTION.ADDRESS, val=address))


def normalize_notes(notes: str) -> str:
    if valid(notes):
        return notes
    else:
        return exceptions_manager.handle_exception(NException(attr=NEXCEPTION.NOTES, val=notes))


def normalize_name(name: str) -> str:
    if valid(name):
        return name.upper()
    else:
        return exceptions_manager.handle_exception(NException(attr=NEXCEPTION.NAME, val=name))


def normalize_zipcode(zipcode: str) -> str:
    if valid(zipcode):
        ZIPCODE_DIGITS = 5

        if len(zipcode) == ZIPCODE_DIGITS:
            return zipcode
        elif len(zipcode) < ZIPCODE_DIGITS:
            prefix = (ZIPCODE_DIGITS - len(zipcode)) * '0'
            return '{}{}'.format(prefix, zipcode)
    else:
        return exceptions_manager.handle_exception(NException(attr=NEXCEPTION.ZIPCODE, val=zipcode))


def normalize_timestamp(timestamp: str) -> Union[datetime.time, str]:
    if valid_timestamp(timestamp):
        try:
            date = parse_date(timestamp)
            updated_time = localize_timezone(date, 'US/Pacific', 'US/Eastern')
            return updated_time.isoformat()
        except ValueError as e:
            # raised when date is unparseable
            return exceptions_manager.handle_exception(NException(attr=NEXCEPTION.TIMESTAMP, val=timestamp))
    else:
        return exceptions_manager.handle_exception(NException(attr=NEXCEPTION.TIMESTAMP, val=timestamp))


