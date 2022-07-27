from apscheduler.schedulers.blocking import BlockingScheduler
import json
import time
import requests
import os
import sqlite3

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=1)
def youtube():
    with open("file.txt", "r+") as f:
        print(f.read())
        f.write(time.strftime("%Y-%m-%d %H:%M:%S"))
        f.close()

sched.start()
