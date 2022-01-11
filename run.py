import os
import json
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", title_page="Home")


@app.route("/about")
def about():
    data = []
    with open("data/company.json","r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", title_page="About", company = data)


@app.route("/contact")
def contact():
    return render_template("contact.html", title_page="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", title_page="careers")



if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)#must be changed to fale before deployments of final site