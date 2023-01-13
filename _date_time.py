from datetime import datetime


def today_date():
    now = datetime.now()
    c_date = now.strftime("%Y-%m-%d")
    #print(f"Today's Date: {c_date}")
    return c_date


def current_time():
    now = datetime.now()
    c_time = now.strftime("%H-%M-%S")
    #print(f"Current Time: {c_time}")
    return c_time
