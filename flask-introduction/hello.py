from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello World, Welcome to the home page!</p>"

@app.route("/another")
def another():
    return "<p>Hello World, Welcome to another page!</p>"

if __name__ == "__main__":
    app.run()