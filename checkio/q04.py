from datetime import datetime

"""
https://py.checkio.org/en/mission/convert-date/

Olhar no chatgpt as várias formas de fazer essa questão e colocar aqui todas as formas possíveis.

from datetime import datetime

def convert_date(date: str) -> str:
    try:
        # Try to parse the date and format it in the desired format
        return datetime.strptime(date, "%d/%m/%Y").strftime("%Y-%m-%d")
    except ValueError:
        # If parsing fails, return an error message
        return "Error: Invalid date."


"""


def is_leap_year(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def convert_date(date: str) -> str:
    parts = date.split("/")

    if len(parts) != 3:
        return "Error: Invalid date."

    day, month, year = parts

    if not day.isdigit() or not month.isdigit() or not year.isdigit():
        return "Error: Invalid date."

    day, month, year = int(day), int(month), int(year)

    if year < 1000 or year > 9999 or month < 1 or month > 12 or day < 1 or day > 31:
        return "Error: Invalid date."

    if month == 2 and (day > 29 or (day == 29 and not is_leap_year(year))):
        return "Error: Invalid date."

    if month in [4, 6, 9, 11] and day > 30:
        return "Error: Invalid date."

    return f"{year:04d}-{month:02d}-{day:02d}"


def convert_date_v2(date: str) -> str:
    try:
        return datetime.strptime(date, "%d/%m/%Y").strftime("%Y-%m-%d")
    except ValueError:
        return "Error: Invalid date."


# These "asserts" are used for self-checking
assert convert_date("25/12/2021") == "2021-12-25"
assert convert_date("01/01/2000") == "2000-01-01"
assert convert_date_v2("15/06/1995") == "1995-06-15"
assert convert_date("29/02/2020") == "2020-02-29"
assert convert_date("10/10/2010") == "2010-10-10"
assert convert_date("31/05/1985") == "1985-05-31"
assert convert_date("07/08/1960") == "1960-08-07"
assert convert_date("02/09/1999") == "1999-09-02"
assert convert_date("30/04/1975") == "1975-04-30"
assert convert_date_v2("29/02/2019") == "Error: Invalid date."
assert convert_date("30/04/1975/1") == "Error: Invalid date."

print("The mission is done! Click 'Check Solution' to earn rewards!")
