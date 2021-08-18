import math

def add_time(start, duration, *args):
    
    # test if user supplied argument to view the day; the day
    # variable will either be a string or a Boolean
    if (len(args) > 0):

        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday' \
            'sunday']
        day = args[0].lower()
        start_date = days.index(day)
    else:
        day = False

    # split the start time, "hh:mm AM/PM", and extract
    # relevant values
    start = start.split(":")
    starting_hour = int(start[0])
    starting_minute = int(start[1].split()[0])
    am_pm = start[1].split()[1]

    hour_to_add = duration.split(":")[0]
    minute_to_add = duration.split(":")[1]
    
    # integer divide the number of hours to add to show how many
    # days (24 hour periods) were added
    days_later = (int(hour_to_add) // 24)
    
    new_hour = int(starting_hour) + int(hour_to_add)
    new_minute = int(starting_minute) + int(minute_to_add)

    # the largest (legal) minute sum possible is 59+59, so at most,
    # the hour increments by 1
    if (new_minute > 59):
        new_hour += 1
        new_minute %= 60

    if (new_hour > 12):
        new_hour %= 12

        if (am_pm == "PM"):
            am_pm = "AM"

            # increment the days_later variable because the time went from
            # a PM time to an AM time
            days_later += 1
            if (day != False):
                day = days[(start_date + 1) % len(days)]
        else:
            am_pm = "PM"

    # modular arithmetic makes a value of 12 AM impossible (12 % 12 == 0),
    # so set new_hour accordingly
    if (new_hour == 0):
        new_hour = 12

    # format output based on if the date was included or not
    if (day != False):
        new_time = f"{new_hour}:{new_minute} {am_pm}, {day.capitalize()}"
    else:
        new_time = f"{new_hour}:{new_minute} {am_pm}"

    if (days_later > 1):
        new_time += f" ({days_later} days later)"
    
    return new_time
