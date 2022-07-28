from apscheduler.schedulers.blocking import BlockingScheduler
import json
import time
import requests
import os
import random

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=60)
def youtube():
    value = 0
    res = requests.get("https://youtube.googleapis.com/youtube/v3/videos?part=snippet&chart=mostPopular&maxResults=25&regionCode=IN&videoCategoryId=10&key=AIzaSyCstEcJGLLkUkilNnRAy4CsRfxfqgVH3R4")
    resJson = res.json()
    body = {}
    if("error" not in resJson):
        for items in resJson["items"]:
            items["snippet"]["description"] = ""
            items["snippet"]["tags"] = ""
            items["snippet"]["thumbnails"] = ""
            items["snippet"]["localized"] = ""
        value += 1
    body["trending"] = resJson
    res = requests.get("https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&q=top%20telugu%20songs&regionCode=IN&type=video&videoCategoryId=10&videoDuration=medium&key=AIzaSyCstEcJGLLkUkilNnRAy4CsRfxfqgVH3R4")
    resJson = res.json()
    if("error" not in resJson):
        for items in resJson["items"]:
            items["snippet"]["description"] = ""
            items["snippet"]["thumbnails"] = ""
        value += 1
    body["telugu"] = resJson
    res = requests.get("https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&q=top%20hindi%20songs&regionCode=IN&type=video&videoCategoryId=10&videoDuration=medium&key=AIzaSyCstEcJGLLkUkilNnRAy4CsRfxfqgVH3R4")
    resJson = res.json()
    if("error" not in resJson):
        for items in resJson["items"]:
            items["snippet"]["description"] = ""
            items["snippet"]["thumbnails"] = ""
        value += 1
    body["hindi"] = resJson
    res = requests.get("https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&q=top%20english%20songs&regionCode=IN&type=video&videoCategoryId=10&videoDuration=medium&key=AIzaSyCstEcJGLLkUkilNnRAy4CsRfxfqgVH3R4")
    resJson = res.json()
    if("error" not in resJson):
        for items in resJson["items"]:
            items["snippet"]["description"] = ""
            items["snippet"]["thumbnails"] = ""
        value += 1
    body["english"] = resJson
    body["time"] = time.strftime("%Y-%m-%d %H:%M:%S")
    if(value == 4):
        res = requests.post("https://my-website-14.000webhostapp.com/", json=body)
        print(res.status_code)
    
    
@sched.scheduled_job('interval', minutes=30)
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
    
    apiKeys = [
        "ee23a57e1fdd4929a9f44f841dd25c69",
        "da484a6c59e04f73ad537ed065b0ee72",
        "ce01e1789e304cfa9092d2c83bb634a0",
        "c388c3135e4741dd9f83ffc330c11fe1",
        "b1c3b0b783c5457bb3441359edb47996",
        "5075193ec6e6477f81db61fd5da9adf7"
    ]
    global n

    def getNews(category, apiKey):
        global n
        res = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&category={category}&pageSize=25&apiKey={apiKey}")
        res = res.json()
        if(n < 5):
            if(res["status"] == "ok"):
                return res
            else:
                n += 1
                apiKey = random.choice(apiKeys)
                return getNews(category, apiKey)
        return "null"

    for category in categories:
        n = 0
        r = getNews(category, random.choice(apiKeys))
        if(r != "null"):
            newRes = {}
            newRes["category"] = category
            newRes["time"] = time.strftime("%Y-%m-%d %H:%M:%S")
            newRes["body"] = r
            res = requests.post("https://my-website-14.000webhostapp.com/news.php", json=newRes)
            print(category+" "+str(n)+" "+res.text)
    
sched.start()
