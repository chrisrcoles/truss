from enum import Enum

class TransformFileNotFoundError(BaseException):
    pass

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
            return print('\nCSV Parsed without errors.\n')

        print('\n')
        for exception in self.exceptions:
            print('Exception for `{}` found for value `{}.`'.format(exception.attr, exception.val))
        print('\nAll rows with errors have been dropped.\n')



ExceptionsManager()
