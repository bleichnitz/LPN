from datetime import datetime


def today_date():
    now = datetime.now()
    c_date = now.strftime("%Y-%m-%d")
    return c_date


def current_time():
    now = datetime.now()
    c_time = now.strftime("%H-%M-%S")
    return c_time


def school_year():
    now = datetime.now()
    c_year = now.year
    c_month = now.month
    if c_month <= 6:
        current_school_year = f"{c_year-1}-{c_year}"
    else:
        current_school_year = f"{c_year}-{c_year+1}"
        # print(c_month)

    return current_school_year