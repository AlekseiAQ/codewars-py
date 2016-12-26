import datetime as dt


def date_nb_days(a0, a, p):
    days = 0
    while a0 < a:
        days += 1
        a0 += a0 * (p / 36000)
    start_date = dt.date(2016, 1, 1)
    new_date = start_date + dt.timedelta(days)
    return new_date.isoformat()
