import datetime

def pluralize(word):
    return word + "s"

def removezeros(s):
    return str(int(s))

def date_time(time):
    date_obj = datetime.datetime.strptime(time, "%d.%m.%Y %H:%M")
    day = date_obj.day
    hour = removezeros(date_obj.hour)
    mins = removezeros(date_obj.minute)
    hour_label = "hour"
    mins_label = "minute"
    if int(hour) != 1:
        hour_label = pluralize(hour_label)

    if int(mins) != 1:
        mins_label = pluralize(mins_label)

    return date_obj.strftime("{} %B %Y year {} {} {} {}".format(day, hour, hour_label, mins, mins_label))

def test():
    testeql(date_time("01.01.2000 00:00"), "1 January 2000 year 0 hours 0 minutes")
    testeql(date_time("19.09.2999 01:59"), "19 September 2999 year 1 hour 59 minutes")
    testeql(date_time("21.10.1999 18:01"), "21 October 1999 year 18 hours 1 minute")
