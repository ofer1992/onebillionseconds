import datetime as dt

my_birth_date_time = dt.datetime(1992, 8, 27, 4, 30, 0)

one_billion_seconds_later = my_birth_date_time + dt.timedelta(seconds=1_000_000_000)

one_billion_seconds_later.strftime('%Y-%m-%d %H:%M:%S')  # '2024-05-04 16:46:40'