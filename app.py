from flask import Flask, request
from newspaper import Article
from googletrans import Translator
import json

app = Flask(__name__)

@app.route('/')
def hello():
    return "ok"

@app.route('/news', methods=['POST'])
def news():
    url = request.form["url"]
    lang = request.form["lang"]
    article = Article(url)
    article.download()
    article.parse()
    translator = Translator()
    text = ""
    keywords = article.meta_keywords
    if(lang == "en"):
        text = article.text
    else:
        text = translator.translate(article.text, dest=lang).text
    return {"text": text, "keywords": keywords, "title": article.title, "img_url": article.top_image}

if __name__ == '__main__':
    app.run()
