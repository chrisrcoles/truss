import re

def valid_duration(time: str) -> bool:
    valid = False
    match = re.match(r'(\d+)\:(\d{2})\:(\d{2})', time)

    if match:
        valid = True

    return valid

def valid_timestamp(timestamp: str) -> bool:
    valid = True

    if not timestamp:
        valid = False

    return valid


def valid(attribute: str) -> bool:
    valid = True

    return valid


def valid_iso_format_timestamp(timestamp: str) -> bool:
    valid = False
    match = re.match(r'(\d{4})-(\d{2})-(\d{2})T(\d{2})\:(\d{2})\:(\d{2})-(\d{2})\:(\d{2})', timestamp)

    if match:
        valid = True

    return valid