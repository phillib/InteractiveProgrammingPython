import time

t = time.time()

def is_leap_year(years):
    if (years % 4 == 0 and years % 100 != 0) or years % 400 == 0:
        return True
    else:
        return False

def day_month(months):
    if months in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif months == 2:
        return 2
    else:
        return 30

def UTC(time):
    """
    convert time to UTC time
    """

    seconds = int(time) % 60
    minutes = int(time) % 3600 // 60
    hours = int(time) % 86400 // 3600

    years = int(time) // 86400 // 365 + 1970

    days_added = 0
    for i in range(1970, years):
        if is_leap_year(i):
            days_added += 366
        else:
            days_added += 365

    day_left = (int(time) // 86400 - days_added)
    day_year = 0
    for i in range(1, 13):
        if day_month(i) == 2:
            if is_leap_year(years):
                day_year += 29
            else:
                day_year += 28
        else:
            day_year += day_month(i)
        if day_year >= day_left:
            months = i
            break

    days = int(time) // 86400 % days_added - day_year + day_month(months) + 1

    date = {"hour":hours,
            "minute":minutes,
            "second":seconds,
            "month":months,
            "day":days,
            "year":years}
    return date



print(UTC(t))
