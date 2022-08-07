from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return redirect(url_for("login")) 


@app.route("/sign-up")
def sign_up():
    return render_template("sign-up.html")


@app.route("/login")
def login():
    return render_template("login.html") 
