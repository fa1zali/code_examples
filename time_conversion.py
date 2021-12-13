#Given a time in -hour AM/PM format, convert it to military (24-hour) time.
# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

def timeConversion(s):
    # Write your code here
    time = s.split(":")
    am_or_pm =  time[2][2:]
    if am_or_pm == 'AM':
        if time[0] == '12':
            time[0] = '00'
    else:
        if time[0] == '12':
            pass
        else:
            time[0] = str(int(time[0]) + 12)
    time[2] = time[2][:-2]
    print(":".join(time))

timeConversion(s = '06:40:03AM')
