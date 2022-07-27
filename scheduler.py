from apscheduler.schedulers.blocking import BlockingScheduler
import json
import time
import requests
import os
import sqlite3

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=1)
def youtube():
    s = json.dumps({"data": "test"})
    conn = sqlite3.connect('database.sqlite')
    cursor = conn.cursor()
    cursor.execute("create table if not exists youtube (data text)")
    cursor.execute("insert into youtube values ('{}')".format(s))
    conn.commit()
    conn.close()
    print("Done")

sched.start()
