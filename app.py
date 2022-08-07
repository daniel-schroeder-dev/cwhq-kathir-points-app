from flask import Flask, render_template, redirect, url_for, session, request

app = Flask(__name__)
app.secret_key = "yZ)mDIC};iv+g0H"


@app.route("/")
def home():
    return redirect(url_for("login"))


@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    return render_template("sign-up.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["is_logged_in"] = True
        return redirect(url_for("admin"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    session["is_logged_in"] = False
    return redirect(url_for("login"))


@app.route("/admin")
def admin():
    return render_template("admin.html")


# Admin endpoints
@app.route("/users")
def users():
    return ""


@app.route("/points")
def points():
    return ""


@app.route("/activities")
def activities():
    return ""


@app.route("/rewards")
def rewards():
    return ""


@app.route("/requests")
def requests():
    return ""


@app.route("/messages")
def messages():
    return ""


@app.route("/roles")
def roles():
    return ""


@app.route("/db-dump")
def db_dump():
    return ""
