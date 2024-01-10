from flask import Flask, render_template
from post import Post
import requests

post_url ="https://api.npoint.io/c790b4d5cab58020d391"

post_data = requests.get(post_url).json()
post_list = [Post(post_id=post["id"],
                  title=post["title"],
                  subtitle=post["subtitle"],
                  body=post["body"]) for post in post_data]

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", post_list = post_list)

@app.route('/post/<int:index>')
def show_post(index):
    return render_template("post.html",  post= post_list[index-1])


if __name__ == "__main__":
    app.run(debug=True)
