import csv
import os
import sys

from io import TextIOWrapper
from typing import Union, List, Tuple

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

def get_files() -> Tuple[str, str]:
    file_to_write = 'output.csv'

    if not len(sys.argv) > 1:
        raise FileNotFoundError

    file_to_transform = sys.argv[1]

    if not os.path.exists(file_to_transform):
        raise FileNotFoundError

    if len(sys.argv) > 2:
        file_to_write = sys.argv[2]

    return (file_to_write, file_to_transform)

