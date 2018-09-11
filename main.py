#!/usr/bin/env python
import csv
import os
from typing import Sequence

import sys

from csvparser.lib.exceptions import ExceptionsManager
from csvparser.lib.normalizers import normalize_duration, normalize_timestamp, normalize_address, normalize_zipcode, \
    normalize_name, normalize_total_duration, normalize_notes
from csvparser.lib.parser import write_header, write_body, get_stdin_buffer, convert_to_csv, create_string

exceptions_manager = ExceptionsManager.getInstance()


def normalize_csv_header(is_header: bool, row: Sequence[str]):
    if is_header:
        write_header(row)


def normalize_csv_body(is_body: bool, row: Sequence[str]):
    if is_body:
        timestamp, address, zipcode, full_name, foo, bar, total, notes = \
            row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]

        foo_duration = normalize_duration(foo, 'foo')
        bar_duration = normalize_duration(bar, 'bar')

        write_body(
            foo_duration,
            bar_duration,
            normalize_timestamp(timestamp),
            normalize_address(address),
            normalize_zipcode(zipcode),
            normalize_name(full_name),
            normalize_total_duration(foo_duration, bar_duration),
            normalize_notes(notes)
        )


def normalize_csv(csv_file: str) -> str:
    for idx, row in enumerate(csv_file):
        normalize_csv_header(idx == 0, row)
        normalize_csv_body(idx != 0 and len(row) != 0, row)



def normalize():
    if len(sys.argv) > 1:
        if os.path.exists(sys.argv[1]):
            with open(sys.argv[1], encoding="utf8", errors='replace') as csvfile:
                return normalize_csv(csv_file=csv.reader(csvfile, delimiter=','))

    return normalize_csv(csv_file=convert_to_csv(string=create_string(stream=get_stdin_buffer())))




if __name__ == "__main__":
    normalize()
    exceptions_manager.raise_exception_warnings()

