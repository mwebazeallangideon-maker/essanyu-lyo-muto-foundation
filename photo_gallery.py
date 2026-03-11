@app.route("/gallery", methods=["GET","POST"])
def gallery():

    if request.method == "POST":

        file = request.files["photo"]

        if file:

            path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(path)

            new_photo = Gallery(filename=file.filename)

            db.session.add(new_photo)
            db.session.commit()

    photos = Gallery.query.all()

    return render_template("gallery.html", photos=photos)