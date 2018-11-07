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

    def isBeforeDate(self, date):
        if self.year < date.year or (self.year == date.year and self.month < date.month) or (self.year == date.year and self.month == date.month and self.day < date.day):
            return True
        else:
            return False

    def __str__(self) -> str:
        return "Date day: " + str(self.day) + ", month: " + str(self.month) + ", year: " + str(self.year)
