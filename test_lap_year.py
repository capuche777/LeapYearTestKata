"""
- Can call lap year
- return false fot not divisible by 4
- return true for divisible by 4 but not 100 or 400
- returns false for divisible by 4 but is divisible by 100 but not 400
- returns true for divisible by 4, divisible by 100, and divisible by 400
"""


def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True

    return False


def check_leap_year(year, expected):
    ret_val = leap_year(year)
    assert ret_val == expected


def test_return_false_not_divisible_by_4():
    check_leap_year(1995, False)


def test_return_true_divisible_by_4():
    check_leap_year(1996, True)


def test_return_false_divisible_by_4_and_100():
    check_leap_year(2100, False)


def test_return_true_divisible_by_4_and_100():
    check_leap_year(2000, True)
