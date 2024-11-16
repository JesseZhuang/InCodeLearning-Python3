# should not name file same as module name datetime
import datetime as dt
import time as tm

# time returns the current time in seconds since the Epoch. (January 1st, 1970)
print('time', tm.time())

# Convert the timestamp to datetime.
dtnow = dt.datetime.fromtimestamp(tm.time())
print('datetime object', dtnow)
print(dtnow.year, dtnow.month, dtnow.day, dtnow.hour,
      dtnow.minute, dtnow.second)

delta = dt.timedelta(days=100)
today = dt.date.today()
print('100 days ago', today - delta)
print(today > today - delta)
