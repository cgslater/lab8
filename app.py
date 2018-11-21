from flask import Flask, render_template, redirect, g, url_for, session
from flask import Markup
from flask import request
MyApp = Flask(__name__)
MyApp.secret_key = "terrible key"
@MyApp.route("/")
def renderThing():
	return render_template("main.html")

@MyApp.route("/about")
def about():
	return render_template("about.html")

@MyApp.route("/contact")
def contact():
	return render_template("contact.html")

@MyApp.route("/picture")
def picture():
	return render_template("picture.html")

@MyApp.route("/login", methods=["GET","POST"])
def login():
	if request.method == "POST":
		session.pop("user",None)

		if request.form["password"] == "password":
			session["user"] = request.form["username"]
			return redirect(url_for("protected")) 

	return render_template("login.html")


@MyApp.route("/joke")
def joke():
	return render_template("joke.html")

@MyApp.route("/protected")
def protected():
	if g.user:
		return render_template("protected.html")

	return redirect(url_for("login")) 

@MyApp.before_request
def before_request():
	g.user = None
	if "user" in session:
		g.user = session["user"]


if __name__ == "__main__":
        MyApp.run(debug=True)

