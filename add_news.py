from app import app
from flask import render_template
@app.route("/admin/add_news", methods=["GET","POST"])
def add_news():

    if request.method == "POST":

        title = request.form["title"]
        content = request.form["content"]

        news = News(title=title, content=content)

        db.session.add(news)
        db.session.commit()

        return redirect("/news")

    return render_template("admin/add_news.html")
