@app.route("/")
def home():

    news = News.query.all()
    events = Event.query.all()

    return render_template("home.html", news=news, events=events)

