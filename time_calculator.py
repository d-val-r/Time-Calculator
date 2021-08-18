import math

def add_time(start, duration, *args):
    
    # test if user supplied argument to view the day; the day
    # variable will either be a string or a Boolean
    if (len(args) > 0):
        day = args[0]
        start_date = days.indexof(day)
    else:
        day = False



    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday' \
            'Sunday']


    # split the start time, "hh:mm AM/PM", and extract
    # relevant values
    start = start.split(":")
    starting_hour = start[0]
    starting_minute = start[1].split()[0]
    am_pm = start[1].split()[1]


    hour_to_add = duration.split()[0]
    minute_to_add = duration.split()[1]

    new_hour = starting_hour + hour_to_add
    new_minute = starting_minute + minute_to_add

    # the largest (legal) minute sum possible is 59+59, so at most,
    # the hour increments by 1
    if (new_minute > 59):
        new_hour += 1
        new_minute %= 60

    if (new_hour > 12):
        new_hour %= 12

        if (am_pm == "PM"):
            am_pm = "AM"
            if (day != False):
                day = days[(start_date + 1) % len(days)]
        else:
            am_pm = "PM"

    # format output based on if the date was included or not
    if (day != False):
        new_time = f"{new_hour}:{new_minute} {am_pm}, {day}"
        difference = math.abs(start_time - days.indexof(day))
        if (difference > 1):
            new_time += f" ({difference} days later)"
    else:
        new_time = f"{new_hour}:{new_minute} {am_pm}"
