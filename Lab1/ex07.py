"""def updateFebruaryInCalendarIfBisectYear(year):
    if year % 4 == 0:
        months['feb'] += 1
"""

# not sure if better keep this local and update with method above if needed.
# need kind of local update for february depending on year
months = {
    'jan': 31,
    'feb': 28,
    'mar': 31,
    'apr': 30,
    'may': 31,
    'jun': 30,
    'jul': 31,
    'aug': 31,
    'sep': 30,
    'oct': 31,
    'nov': 30,
    'dec': 31
}

monthsName = ['jan', 'feb', 'mar', 'apr',
              'may', 'jun', 'jul', 'aug',
              'sep', 'oct', 'nov', 'dec']


def dateFromYearAndDayInYearUtil(year, dayInYear):
    if year % 4 == 0:
        months['feb'] = 29

    date = {'day': None, 'month': None, 'year': None}

    for monthName in monthsName:
        daysInCurrentMonth = months[monthName]
        # print(dayInYear)
        if dayInYear > daysInCurrentMonth:
            dayInYear -= daysInCurrentMonth
        else:
            date['day'] = dayInYear
            date['month'] = monthName
            date['year'] = year
            break
    return date


def dateFromYearAndDayInYear(year, dayInYear):
    day = dateFromYearAndDayInYearUtil(year, dayInYear)['day']
    month = dateFromYearAndDayInYearUtil(year, dayInYear)['month']
    year = dateFromYearAndDayInYearUtil(year, dayInYear)['year']

    return str(year) + ' ' + str(month) + ' ' + str(day)


yearFromConsole = input("year = ")
dayFromConsole = input("day = ")
print(dateFromYearAndDayInYear(int(yearFromConsole), int(dayFromConsole)))
