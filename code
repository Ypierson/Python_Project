import pyodbc
cnxn = pyodbc.connect(r'Driver=SQL Server;Server=balt-sql311-prd;Database=DOT_DATA;Trusted_Connection=yes;')
cursor = cnxn.cursor()
cursor.execute("SELECT TOP (1000) [ACRSREPORTTIMESTAMP],[CRASHDATE],[CRASHTIME] FROM [DOT_DATA].[dbo].[acrs_crash]")
while 1:
    row = cursor.fetchone()
    if not row:
        break
    print(row.CRASHTIME)
cnxn.close()
