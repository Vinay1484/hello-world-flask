from apscheduler.schedulers.blocking import BlockingScheduler
import json
import time
import requests

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=1)
def youtube():
    res = requests.get("https://youtube.googleapis.com/youtube/v3/videos?part=snippet&chart=mostPopular&maxResults=25&regionCode=IN&videoCategoryId=10&key=AIzaSyCstEcJGLLkUkilNnRAy4CsRfxfqgVH3R4")
    resJson = res.json()
    body = {}
    for items in resJson["items"]:
        items["snippet"]["description"] = ""
        items["snippet"]["tags"] = ""
        items["snippet"]["thumbnails"] = ""
        items["snippet"]["localized"] = ""
    body["trending"] = resJson
    res = requests.get("https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&q=top%20telugu%20songs&regionCode=IN&type=video&videoCategoryId=10&videoDuration=medium&key=AIzaSyCstEcJGLLkUkilNnRAy4CsRfxfqgVH3R4")
    resJson = res.json()
    for items in resJson["items"]:
        items["snippet"]["description"] = ""
        items["snippet"]["thumbnails"] = ""
    body["telugu"] = resJson
    res = requests.get("https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&q=top%20hindi%20songs&regionCode=IN&type=video&videoCategoryId=10&videoDuration=medium&key=AIzaSyCstEcJGLLkUkilNnRAy4CsRfxfqgVH3R4")
    resJson = res.json()
    for items in resJson["items"]:
        items["snippet"]["description"] = ""
        items["snippet"]["thumbnails"] = ""
    body["hindi"] = resJson
    res = requests.get("https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&q=top%20english%20songs&regionCode=IN&type=video&videoCategoryId=10&videoDuration=medium&key=AIzaSyCstEcJGLLkUkilNnRAy4CsRfxfqgVH3R4")
    resJson = res.json()
    for items in resJson["items"]:
        items["snippet"]["description"] = ""
        items["snippet"]["thumbnails"] = ""
    body["english"] = resJson
    body["time"] = time.strftime("%Y-%m-%d %H:%M:%S")

    with open("data.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(body))
        f.close()
    print("Done")

sched.start()
