import csv
import sys

from io import TextIOWrapper
from typing import Union, List

Csvstream = Union[List, TextIOWrapper]

def get_stdin_buffer() -> bytes:
    return sys.stdin.buffer.read()


def create_string(stream: bytes, format='utf-8', errors='replace') -> str:
    # https://docs.python.org/3/howto/unicode.html
    return stream.decode(format, errors)


def get_csv_reader(string: Csvstream) -> str:
    return csv.reader(string, delimiter=',')


def get_csv_writer(file: TextIOWrapper) -> csv.writer:
    return csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

def write_to_csv(writer, string: str) -> None:
    writer.write(string)



