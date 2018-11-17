from datetime import date

from main.Exception import InvalidDateFormatException


class Date:
    """
    Models date having day (0 < int < 31), month (0 < int < 13), year(int > 0)
    """

    def __init__(self, day, month, year) -> None:
        if type(day) == int:
            if 0 < day < 31:
                self.day = day
            else:
                raise InvalidDateFormatException
        else:
            raise InvalidDateFormatException

        if type(month) == int:
            if 0 < month < 13:
                self.month = month
            else:
                raise InvalidDateFormatException
        else:
            raise InvalidDateFormatException

        if type(year) == int:
            if 0 < year:
                self.year = year
            else:
                raise InvalidDateFormatException
        else:
            raise InvalidDateFormatException

    def __eq__(self, other: "Date"):
        return self.day == other.day and self.month == other.month and self.year == other.year

    def isBeforeDate(self, dateUntil):
        """
        Checks whether self is before date

        :param dateUntil: the date to compare to
        :return: True if self is before date, False otherwise
        """
        if self.year < dateUntil.year or (self.year == dateUntil.year and self.month < dateUntil.month) or (self.year == dateUntil.year and self.month == dateUntil.month and self.day < dateUntil.day):
            return True
        else:
            return False

    def daysUntilDate(self, dateUntil: "Date"):
        d1 = date(self.year, self.month, self.day)
        d2 = date(dateUntil.year, dateUntil.month, dateUntil.day)
        delta = d1 - d2
        return abs(delta.days)

    def __str__(self) -> str:
        return "Date day: " + str(self.day) + ", month: " + str(self.month) + ", year: " + str(self.year)
