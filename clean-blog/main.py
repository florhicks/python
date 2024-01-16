from flask import Flask, render_template, request
import requests
import datetime
from contact import Email

app = Flask(__name__)

posts = requests.get("https://api.npoint.io/e09b81e5bc7a2a6f6564").json()

@app.route("/")
def home():
    current_year = datetime.datetime.now().year
    return render_template("index.html", posts = posts, current_year=current_year)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<int:index>")
def render_post(index):
    requested_post = posts[index-1]
    return render_template("post.html", post = requested_post)

@app.route("/contact", methods =["GET","POST"])
def receive_data():
    if request.method == "POST":
        msg = Email(name=request.form["name"],
                    email_address=request.form["email"],
                    phone_number=request.form["phone"],
                    message=request.form["message"])
        return render_template("contact.html", success = "Successfully sent your message!")



if __name__ == "__main__":
    app.run(debug=True)
