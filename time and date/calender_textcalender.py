import calendar

cal = calendar.TextCalendar(calendar.SUNDAY)


for month in range(1, 13):
    cal.prmonth(2022, month)
