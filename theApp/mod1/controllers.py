from flask import Blueprint, request, render_template

mod1= Blueprint("auth", __name__, url_prefix="/auth")

@mod1.route("hello")
def hello():
	return render_template("mod1/hello.html")
