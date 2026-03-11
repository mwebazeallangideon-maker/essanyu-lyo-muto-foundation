from app import app
from flask import render_template

@app.route("/")
def home():

    news = News.query.all()
    events = Event.query.all()

    return render_template("home.html", news=news, events=events)

