import pyodbc
Hours = 48
cnxn = pyodbc.connect(r'Driver=SQL Server;Server=balt-sql311-prd;Database=DOT_DATA;Trusted_Connection=yes;')
cursor = cnxn.cursor()
cursor.execute("SELECT TOP (1) [ACRSREPORTTIMESTAMP],[CRASHDATE],[CRASHTIME] FROM [DOT_DATA].[dbo].[acrs_crash]")
while 1:
    row = cursor.fetchone()
    if not row:
        break
    print(row.CRASHTIME, row.CRASHDATE)
cnxn.close()

 import datetime
first_time = datetime.datetime.now()
later_time = datetime.datetime.now()
difference = later_time - first_time
datetime.timedelta(0, 8, 562000)
days    = divmod(duration_in_s, 86400)        # Get days (without [0]!)
hours   = divmod(days[1], 3600)               # Use remainder of days to calc hours
minutes = divmod(hours[1], 60)                # Use remainder of hours to calc minutes
seconds = divmod(minutes[1], 1)               # Use remainder of minutes to calc seconds
print("Time between dates: %d days, %d hours, %d minutes and %d seconds" % (days[0], hours[0], minutes[0], seconds[0]))






