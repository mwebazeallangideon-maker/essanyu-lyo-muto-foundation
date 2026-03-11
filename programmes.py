from app import app
from flask import render_template
@app.route("/programmes")
def programmes():
    return render_template("programmes.html")
