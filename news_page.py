from app import app
from flask import render_template
@app.route("/news")
def news():

    news = News.query.all()

    return render_template("news.html", news=news)
