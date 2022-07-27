from apscheduler.schedulers.blocking import BlockingScheduler
import json
import time
import requests
import os

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=1)
def youtube():
    

    with open("youtube.json", "w", encoding="utf-8") as f:
        f.write(json.dumps({"hello":"hi"}))
        print(os.path.realpath(f.name))
        f.close()
    print("Done")

sched.start()
