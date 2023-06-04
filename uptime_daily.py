from datetime import datetime
# to be updated by the current time


def uptimeDaily(Id):
    daystart = "2023-01-22 07:00:00.000000 UTC"
    hourend = "2023-01-21 7:06:30.123456 UTC"
    # to be entered by the user
    storeid = Id
    datetimestart = datetime.strptime(daystart, "%Y-%m-%d %H:%M:%S.%f UTC")
    datetimeend = datetime.strptime(hourend, "%Y-%m-%d %H:%M:%S.%f UTC")
    f = open("store status.csv", "r")
    data = f.readlines()
    dataAfterSpliting = []
    # splittig the data
    for i in data:
        dataAfterSpliting.append(i.split(","))
    # storing releant data which lies within the given range
    active = []
    inactive = []
    for i in dataAfterSpliting:
        if i[0] == storeid:
            timestamp = i[2][:-1]
            time = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S.%f UTC")
            if(datetimestart > time and datetimeend < time and i[1] == "active"):
                active.append(timestamp)
            elif(datetimestart > time and datetimeend < time and i[1] == "inactive"):
                inactive.append(timestamp)
    active.sort()
    inactive.sort()
    # for i in active:
    #     print(i)

    datetime_obj = datetime.strptime(daystart, "%Y-%m-%d %H:%M:%S.%f %Z")
    day_of_week = datetime_obj.strftime("%w")

    # getting the local time of opening and closing
    f2 = open("Menu hours.csv", "r")
    data2 = f2.readlines()
    localtime = []
    for i in data2:
        localtime.append(i.split(','))
    time_stamp_local = []
    for i in localtime:
        if i[0] == storeid and i[1] == day_of_week:
            time_stamp_local.append(i)
    active.sort()
    print(time_stamp_local)
    # print(active)
    uptimehourly = 0

    alltimestampsinrange = []
    total_hour = 0

    for i in time_stamp_local:
        for j in active:
            starttime = i[2]
            endtime = i[3][:-1]
            starttime = datetime.strptime(
                "2000-01-01 " + starttime, "%Y-%m-%d %H:%M:%S")
            endtime = datetime.strptime(
                "2000-01-01 " + endtime, "%Y-%m-%d %H:%M:%S")
            currenttime = j
            starttime = starttime.strftime("%H:%M:%S")
            endtime = endtime.strftime("%H:%M:%S")
            datetime_obj = datetime.strptime(
                currenttime, "%Y-%m-%d %H:%M:%S.%f %Z")
            time = datetime_obj.strftime("%H:%M:%S")
            currenttime = datetime.strptime(
                "2000-01-01 " + time, "%Y-%m-%d %H:%M:%S")
            print(starttime)
            print(endtime)
            print(time)
            print('\n')
            if str(time) > str(starttime) and str(time) < str(endtime):
                total_hour += 1

    total_inactive_hour = 0
    for i in time_stamp_local:
        for j in inactive:
            starttime = i[2]
            endtime = i[3][:-1]
            starttime = datetime.strptime(
                "2000-01-01 " + starttime, "%Y-%m-%d %H:%M:%S")
            endtime = datetime.strptime(
                "2000-01-01 " + endtime, "%Y-%m-%d %H:%M:%S")
            currenttime = j
            starttime = starttime.strftime("%H:%M:%S")
            endtime = endtime.strftime("%H:%M:%S")
            datetime_obj = datetime.strptime(
                currenttime, "%Y-%m-%d %H:%M:%S.%f %Z")
            time = datetime_obj.strftime("%H:%M:%S")
            currenttime = datetime.strptime(
                "2000-01-01 " + time, "%Y-%m-%d %H:%M:%S")
            # print(starttime)
            # print(endtime)
            # print(time)
            # print('\n')
            if str(time) > str(starttime) and str(time) < str(endtime):
                total_inactive_hour += 1

    return [total_hour, total_inactive_hour]
