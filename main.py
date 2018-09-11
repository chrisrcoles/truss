#!/usr/bin/env python
import os
from typing import Sequence

import sys

from csvparser.lib.exceptions import ExceptionsManager, TransformFileMustExistError
from csvparser.lib.normalizers import normalize_duration, normalize_timestamp, normalize_address, normalize_zipcode, \
    normalize_name, normalize_total_duration, normalize_notes
from csvparser.lib.parser import get_csv_reader, get_csv_writer

exceptions_manager = ExceptionsManager.getInstance()


def normalize_csv_header(is_header: bool, row: Sequence[str], new_csv) -> None:
    if is_header:
        new_csv.writerow(row)


def normalize_csv_body(is_body: bool, row: Sequence[str], new_csv) -> None:
    if is_body:
        timestamp, address, zipcode, full_name, foo, bar, total, notes = \
            row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]

        foo_duration = normalize_duration(foo, 'foo')
        bar_duration = normalize_duration(bar, 'bar')

        new_csv.writerow([
            normalize_timestamp(timestamp), normalize_address(address), normalize_zipcode(zipcode), normalize_name(full_name),
            foo_duration, bar_duration, normalize_total_duration(foo_duration, bar_duration), normalize_notes(notes) ])


def normalize_csv(read_file: str, write_file) -> None:
    for idx, row in enumerate(read_file):
        normalize_csv_header(idx == 0, row, write_file)
        normalize_csv_body(idx != 0 and len(row) != 0, row, write_file)


def normalize() -> None:
    file_to_write = 'output.csv'

    if len(sys.argv) > 1:
        file_to_transform = sys.argv[1]

        if len(sys.argv) > 2:
            file_to_write = sys.argv[2]

        if os.path.exists(file_to_transform):
            with open(file_to_write, mode='w+') as new_csvfile:
                with open(file_to_transform, encoding='utf8', errors='replace') as csvfile:
                    return normalize_csv(get_csv_reader(csvfile), get_csv_writer(new_csvfile))
        raise FileNotFoundError
    else:
        raise TransformFileMustExistError



if __name__ == "__main__":
    normalize()
    exceptions_manager.raise_exception_warnings()
