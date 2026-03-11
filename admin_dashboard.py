@app.route("/admin")
def admin():
    return render_template("admin/dashboard.html")