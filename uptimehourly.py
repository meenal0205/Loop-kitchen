from datetime import datetime
# to be updated by the current time stamp


def uptime(Id):
    hourstart = "2023-01-24 12:05:17.94139 UTC"
    hourend = "2023-01-24 13:05:30.123456 UTC"
    storeid = Id
    datetimestart = datetime.strptime(hourstart, "%Y-%m-%d %H:%M:%S.%f UTC")
    datetimeend = datetime.strptime(hourend, "%Y-%m-%d %H:%M:%S.%f UTC")
    f = open("store status.csv", "r")
    data = f.readlines()
    dataAfterSpliting = []
    # splittig the data
    for i in data:
        dataAfterSpliting.append(i.split(","))
    # storing releant data which lies within the given range
    stampdataActive = []
    stampdataInactive = []
    for i in dataAfterSpliting:
        if i[0] == storeid:
            timestamp = i[2][:-1]
            time = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S.%f UTC")

            if(datetimestart < time and datetimeend > time and i[1] == "active"):
                stampdataActive.append(timestamp)
            if(datetimestart < time and datetimeend > time and i[1] == "inactive"):
                stampdataInactive.append(timestamp)
    # getting the day of week
    # print("Inactive", stampdataInactive)
    datetime_obj = datetime.strptime(hourstart, "%Y-%m-%d %H:%M:%S.%f UTC")
    day_of_week = datetime_obj.strftime("%w")
    # getting the local time of opening and closing
    f2 = open("Menu hours.csv", "r")
    data2 = f2.readlines()
    localtime = []
    for i in data2:
        localtime.append(i.split(','))
    time_stamp_local = []
    for i in localtime:
        if i[0] == storeid and int(i[1] == day_of_week):
            time_stamp_local.append(i)
    stampdataActive.sort()
    # print(time_stamp_local)
    # print(stampdataActive)
    total_active = 0
    for i in time_stamp_local:
        for j in stampdataActive:
            starttime = i[2]
            endtime = i[3][:-1]
            starttime = datetime.strptime(
                "2000-01-01 " + starttime, "%Y-%m-%d %H:%M:%S")
            endtime = datetime.strptime(
                "2000-01-01 " + endtime, "%Y-%m-%d %H:%M:%S")
            currenttime = j
            datetime_obj = datetime.strptime(
                currenttime, "%Y-%m-%d %H:%M:%S.%f %Z")
            time = datetime_obj.strftime("%H:%M:%S")
            currenttime = datetime.strptime(
                "2000-01-01 " + time, "%Y-%m-%d %H:%M:%S")
            if currenttime > starttime and currenttime < endtime:
                uptimehourly = currenttime-starttime
                uptimehourly = str(uptimehourly).split(":")
                total_active = uptimehourly[1]
    # print("time stamp local", time_stamp_local)
    total_inactive = 0
    for i in time_stamp_local:
        for j in stampdataInactive:
            # print("printing j ", j)
            starttime = i[2]
            endtime = i[3][:-1]
            starttime = datetime.strptime(
                "2000-01-01 " + starttime, "%Y-%m-%d %H:%M:%S")
            endtime = datetime.strptime(
                "2000-01-01 " + endtime, "%Y-%m-%d %H:%M:%S")
            currenttime = j
            datetime_obj = datetime.strptime(
                currenttime, "%Y-%m-%d %H:%M:%S.%f %Z")
            time = datetime_obj.strftime("%H:%M:%S")
            currenttime = datetime.strptime(
                "2000-01-01 " + time, "%Y-%m-%d %H:%M:%S")
            if currenttime > starttime and currenttime < endtime:
                uptimehourly = endtime-currenttime
                uptimehourly = str(uptimehourly).split(":")
                total_inactive = uptimehourly[1]
    return [total_active, total_inactive]


# print(uptime("5210062273617208234"))
