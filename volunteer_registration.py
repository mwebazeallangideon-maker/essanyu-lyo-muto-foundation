@app.route("/volunteer", methods=["GET","POST"])
def volunteer():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]

        new_volunteer = Volunteer(name=name, email=email)

        db.session.add(new_volunteer)
        db.session.commit()

        return "Thank you for volunteering!"