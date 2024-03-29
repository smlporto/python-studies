from flask import Flask, render_template
from post import Post
import requests

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", all_posts=post_objects)

@app.route("/post/<int:index>")
def get_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)

# from flask import Flask, render_template
# from datetime import datetime
# import requests

# app = Flask(__name__)

# @app.route("/")
# def home():
#     current_year = datetime.now().year
#     return render_template('index.html', year=current_year)

# @app.route("/guess/<name>")
# def guess(name):
#     response_age = requests.get(f"https://api.agify.io?name={name}")
#     response_gender = requests.get(f"https://api.genderize.io?name={name}")
    
#     age_data = response_age.json()
#     gender_data = response_gender.json()
    
#     name_age = age_data["age"]
#     name_gender = gender_data["gender"]
#     return render_template('guess.html', name=name, age=name_age, gender=name_gender)

# @app.route("/blog/<num>")
# def get_blog(num):
#     response = requests.get(f"https://api.npoint.io/c790b4d5cab58020d391")
#     posts = response.json()
#     return render_template('blog.html', posts=posts)

# if __name__ == "__main__":
#     app.run(debug=True)