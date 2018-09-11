from enum import Enum

from .parser import write_to_stdout, write_new_line


class NEXCEPTION(Enum):
    TIMESTAMP = 1
    ADDRESS = 2
    ZIPCODE = 3
    NAME = 4
    FOO_DURATION = 5
    BAR_DURATION = 6
    TOTAL_DURATION = 7
    NOTES = 8


class NException:
    def __init__(self, attr: Enum, val: str):
        self.attr = attr
        self.val = val


class ExceptionsManager:
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if ExceptionsManager.__instance == None:
            ExceptionsManager()
        return ExceptionsManager.__instance


    def __init__(self):
        self.exceptions = []
        """ Virtually private constructor. """
        if ExceptionsManager.__instance != None:
            raise Exception("This class is a ExceptionsManager!")
        else:
            ExceptionsManager.__instance = self


    def handle_exception(self, exception: NException) -> str:
        self.exceptions.append(exception)
        return self.drop_row()


    def drop_row(self) -> str:
        return ''


    def raise_exception_warnings(self):
        if not len(self.exceptions):
            return write_to_stdout('\nCSV Parsed without errors.\n')

        write_new_line()
        for exception in self.exceptions:
            write_to_stdout('Exception for `{}` found for value `{}.`'.format(exception.attr, exception.val))
        write_new_line()
        write_to_stdout('All rows with errors have been dropped.')
        write_new_line()

ExceptionsManager()
