from apscheduler.schedulers.blocking import BlockingScheduler
import json
import time
import requests
import os
import sqlite3

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=10)
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
    res = requests.post("https://my-website-14.000webhostapp.com/", json=body)
    print(res.status_code)
    
    
@sched.scheduled_job('interval', minutes=15)
def news():
    categories = [
    "business",
    "entertainment",
    "general",
    "health",
    "science",
    "sports",
    "technology"
    ]

    for category in categories:
        res = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&category={category}&pageSize=25&apiKey=ee23a57e1fdd4929a9f44f841dd25c69")
        newRes = {}
        newRes["category"] = category
        newRes["time"] = time.strftime("%Y-%m-%d %H:%M:%S")
        newRes["body"] = res.json()
        res = requests.post("https://my-website-14.000webhostapp.com/news.php", json=newRes)
        print(category+" "+res.text)
    
sched.start()
