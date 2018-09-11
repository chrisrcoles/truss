import csv
import sys
from typing import Sequence


def get_stdin_buffer() -> bytes:
    return sys.stdin.buffer.read()


def write_to_stdout(args: str, out=sys.stdout) -> None:
    out.write(args)


def create_string(stream: bytes, format='utf-8', errors='replace') -> str:
    # https://docs.python.org/3/howto/unicode.html
    return stream.decode(format, errors)


def convert_to_csv(string: str) -> str:
    return csv.reader(string.split('\n'), delimiter=',')


def write_header(header_row: Sequence[str]) -> None:
    for headerIdx, header in enumerate(header_row):
        write_to_file(header)

        if headerIdx == len(header_row) - 1:
            write_new_line()


def write_body(foo: str, bar: str, timestamp: str, address: str, zipcode: str, name: str, total_duration: str, notes: str) -> None:
    write_to_file(timestamp)
    write_to_file(address)
    write_to_file(zipcode)
    write_to_file(name)
    write_to_file(foo)
    write_to_file(bar)
    write_to_file(total_duration)
    write_to_file(notes)
    write_new_line()


def write_to_file(value: str, delimiter: str=',') -> None:
    write_to_stdout('{}{}'.format(value, delimiter))


def write_new_line() -> None:
    write_to_stdout('\n')