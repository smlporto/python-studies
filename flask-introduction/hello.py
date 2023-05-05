from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper_function():
        return "<b>" + function() + "</b>"
    return wrapper_function

def make_emphasis(function):
    def wrapper_function():
        return "<em>" + function() + "</em>"
    return wrapper_function

def make_underlined(function):
    def wrapper_function():
        return "<u>" + function() + "</u>"
    return wrapper_function

@app.route("/")
@make_bold
@make_emphasis
@make_underlined
def hello_world():
    return "<p>Hello World, Welcome to the home page!</p>"

@app.route("/another")
def another():
    return "<p>Hello World, Welcome to another page!</p>"

if __name__ == "__main__":
    app.run(debug=True)