from datetime import datetime


def today_date():
    now = datetime.now()
    c_date = now.strftime("%Y-%m-%d")
    return c_date


def current_time():
    now = datetime.now()
    c_time = now.strftime("%H-%M-%S")
    return c_time
