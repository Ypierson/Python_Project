import pyodbc
Hours = 48
cnxn = pyodbc.connect(r'Driver=SQL Server;Server=balt-sql311-prd;Database=DOT_DATA;Trusted_Connection=yes;')
cursor = cnxn.cursor()
cursor.execute("SELECT TOP (1) [ACRSREPORTTIMESTAMP],[CRASHDATE],[CRASHTIME] FROM [DOT_DATA].[dbo].[acrs_crash] Order BY [ACRSREPORTTIMESTAMP] DESC")
while 1:
    row = cursor.fetchone()
    if not row:
        break
    print(row.ACRSREPORTTIMESTAMP, row.CRASHTIME)
    import pdb;
    pdb.set_trace()
cnxn.close()

import datetime

datetime.datetime.now()
today = datetime.datetime.now()
delta = datetime.timedelta(hours=48)
x = 48

if x >= 48:
print("true")

"""
difference = later_time - first_tim
datetime.timedelta(0, 8, 562000)
days = list()
# Get days (without [0]!)
hours = divmod(days[1], 3600)                Use remainder of days to calc hours
minutes = divmod(hours[1], 60)                # Use remainder of hours to calc minutes
seconds = divmod(minutes[1], 1)               # Use remainder of minutes to calc seconds
print("Time between dates: %d days, %d hours, %d minutes and %d seconds" % (days[0], hours[0], minutes[0], seconds[0]))


today = datetime.datetime("ACRSREPORTTIMESTAMP")
friday = datetime.datetime(2021,6,16)
print(today - friday)

def is_timestamp_recent(timestamp_from_db, num_of_hours):
    
    Determine if the timestamp from the database is old enough that we need to notify
    :param timestamp_from_db: a datetime type that comes from the database we are checking
    :param num_of_hours: the number of hours that we expect an entry in the database, otherwise we notify
    :return bool: True if the timestamp is recent enough that we don't need to notify, false if we should notify
    
    pass
   """