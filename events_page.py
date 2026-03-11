@app.route("/events")
def events():

    events = Event.query.all()

    return render_template("events.html", events=events)