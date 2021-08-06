import pyodbc
Hours = 48
cnxn = pyodbc.connect(r'Driver=SQL Server;Server=balt-sql311-prd;Database=DOT_DATA;Trusted_Connection=yes;')
cursor = cnxn.cursor()
cursor.execute("SELECT TOP (1) [ACRSREPORTTIMESTAMP],[CRASHDATE],[CRASHTIME] FROM [DOT_DATA].[dbo].[acrs_crash] Order BY [ACRSREPORTTIMESTAMP] DESC")
while 1:
    row = cursor.fetchone()
    if not row:
        break
    print(row.CRASHTIME, row.CRASHDATE)
    import pdb;
    pdb.set_trace()
cnxn.close()

import datetime
"""
datetime.datetime.now()
first_time = datetime.datetime.now()
later_time = datetime.datetime.now()
difference = later_time - first_time
datetime.timedelta(0, 8, 562000)
days = list()
# Get days (without [0]!)
hours = divmod(days[1], 3600)                Use remainder of days to calc hours
minutes = divmod(hours[1], 60)                # Use remainder of hours to calc minutes
seconds = divmod(minutes[1], 1)               # Use remainder of minutes to calc seconds
print("Time between dates: %d days, %d hours, %d minutes and %d seconds" % (days[0], hours[0], minutes[0], seconds[0]))


today = datetime.datetime(2021,6,21)
friday = datetime.datetime(2021,6,16)
print(today - friday)
"""

 today + timedelta(hours=48)
datetime.datetimenow()
format_timedelta(timedelta(hours=48, seconds=3700)

import pickle

# obj0, obj1, obj2 are created here...

# Saving the objects:
with open('objs.pkl', 'w') as f:  # Python 3: open(..., 'wb')
    pickle.dump([obj0, obj1, obj2], f)

# Getting back the objects:
with open('objs.pkl') as f:  # Python 3: open(..., 'rb')
    obj0, obj1, obj2 = pickle.load(f)


def my_function_with_args(today, friday):
    print("today - friday" % (today,friday))

    def dif_two_numbers(a, b):
        return a - b
