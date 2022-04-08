import calendar
import sys

year = int(sys.argv[1])

meetings = []

# show every month
for month in range(1, 13):
    # compute the date for each week that overlap the month
    c = calendar.monthcalendar(year, month)
    first_week = c[0]
    second_week = c[1]
    third_week = c[2]
    if first_week[calendar.WEDNESDAY]:
        meeting_date = second_week[calendar.WEDNESDAY]
        meetings.append(meeting_date)
    else:
        meeting_date = third_week[calendar.WEDNESDAY]
        meetings.append(meeting_date)
    print(f"{calendar.month_abbr[month]:>3},{calendar.day_name[month]}, {meeting_date:>2}")
print(f"Meetings: {meetings}")