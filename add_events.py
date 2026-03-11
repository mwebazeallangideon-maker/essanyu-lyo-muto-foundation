@app.route("/admin/add_event", methods=["GET","POST"])
def add_event():

    if request.method == "POST":

        title = request.form["title"]
        description = request.form["description"]

        event = Event(title=title, description=description)

        db.session.add(event)
        db.session.commit()

        return redirect("/events")

    return render_template("admin/add_event.html")