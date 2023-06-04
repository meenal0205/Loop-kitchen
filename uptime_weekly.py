from datetime import datetime, timedelta


def uptime_weekly(ID):
    timestamp = "2023-01-22 07:00:00.000000 UTC"
    datetime_obj = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S.%f %Z")
    total_active = 0
    total_inactive = 0
    datetime_obj -= timedelta(weeks=1)
    f = open("store status.csv", "r")
    data = f.readlines()
    dataAfterSpliting = []
    # splittig the data
    for i in data:
        dataAfterSpliting.append(i.split(","))
    storeid = ID
    for i in range(7):
        current_day = datetime_obj + timedelta(days=i)
        previous_day = current_day - timedelta(days=1)
        formatted_current_day = datetime.strftime(
            current_day, "%Y-%m-%d %H:%M:%S.%f UTC")
        formatted_previous_day = datetime.strftime(
            previous_day, "%Y-%m-%d %H:%M:%S.%f UTC")
        # print("current:", formatted_current_day)
        # print("previous", formatted_previous_day)

        active = []
        inactive = []
        for i in dataAfterSpliting:
            if i[0] == storeid:
                # print(i)
                timestamp = i[2][:-1]
                time = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S.%f UTC")

                # print(datetimestart)
                # print(datetimeend)
                # print(datetime)
                # print("\n")
                if(timestamp > formatted_previous_day and timestamp < formatted_current_day and i[1] == "active"):
                    active.append(timestamp)
                elif(timestamp > formatted_previous_day and timestamp < formatted_current_day and i[1] == "inactive"):
                    inactive.append(timestamp)
        active.sort()
        inactive.sort()
        # print("active", active)
        # print("inactive", inactive)
        # for i in active:
        #     print(i)

        # datetime_obj = datetime.strptime(previous_day, "%Y-%m-%d %H:%M:%S.%f %Z")
        day_of_week = current_day.strftime("%w")
        # print(day_of_week)

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
        # print("local time stamp ", time_stamp_local)

        # print("local time stamp for each day", time_stamp_local)
        # print(active)
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
                # print("starttime", starttime)
                # print("endtime", endtime)
                # print("time", time)
                # print('\n')
                if str(time) > str(starttime) and str(time) < str(endtime):
                    total_inactive += 1

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
                # print("starttime", starttime)
                # print("endtime", endtime)
                # print("time", time)
                # print('\n')
                if str(time) > str(starttime) and str(time) < str(endtime):
                    total_active += 1

        # print("\nend\n")

    return [total_active, total_inactive]


# print(uptime_weekly("5210062273617208234"))
#