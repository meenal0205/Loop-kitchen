from flask import Flask, render_template, request, session, redirect
from flask_mysqldb import MySQL
import MySQLdb
from uptime_weekly import uptime_weekly
from uptime_daily import uptimeDaily
from uptimehourly import uptime
app = Flask(__name__)

app.secret_key = 'meenal123'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'sys'
app.config['TASK_COMPLETED'] = False

db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="sys")
cur = db.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS reports (storeId varchar(50), uptime_hourly int , downtime_hourly int , uptime_daily int , downtime_daily int, uptime_weekly int,downtime_weekly int)")
f = open("bq-results-20230125-202210-1674678181880.csv", "r")
data = f.readlines()


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        storeId = request.form['storeId']
        cur.execute("select * from reports where storeID=%s", [storeId])
        info = cur.fetchone()
        if info != None:
            print(info)
            return render_template("result.html", content=info)
        else:
            hourly = uptime(storeId)
            weekly = uptime_weekly(storeId)
            daily = uptimeDaily(storeId)
            cur.execute("insert into reports values(%s,%s,%s,%s,%s,%s,%s)", (storeId,
                        hourly[0], hourly[1], daily[0], daily[1], weekly[0], weekly[1]))
            db.commit()
            cur.execute("select * from reports where storeID=%s", [storeId])
            info = cur.fetchone()
            print(info)
        return render_template("result.html", content=info)

    return render_template('index.html')


@app.route('/trigger_report', methods=["GET"])
def trigger_report():
    dataAfterSpliting = []
    app.config['TASK_COMPLETED'] = True
    for i in data:
        dataAfterSpliting.append(i.split(","))
    for i in dataAfterSpliting:
        hourly = uptime(i[0])
        weekly = uptime_weekly(i[0])
        daily = uptimeDaily(i[0])
        cur.execute("insert into reports values(%s,%s,%s,%s,%s,%s,%s)", (i[0],
                                                                         hourly[0], hourly[1], daily[0], daily[1], weekly[0], weekly[1]))
        db.commit()

    return render_template('index.html', task_completed=app.config['TASK_COMPLETED'])


if __name__ == "__main__":
    app.run(debug=True)
