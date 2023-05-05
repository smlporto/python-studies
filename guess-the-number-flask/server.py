from flask import Flask
import random

number = random.randint(0, 9)
print(number)

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
            "<img width='500' src='https://media3.giphy.com/media/YYIeKT80xZNzq/giphy.gif?cid=ecf05e472906a0bb80323ca0e45680583678c0190352ba6e&ep=v1_gifs_gifId&rid=giphy.gif&ct=g'>"

@app.route("/<int:guess>")
def guess_number(guess):
    if guess > number:
        return f"<h1>The number is not {guess}</h1>" \
                "<img width='500' src='https://media0.giphy.com/media/LFA6Qbj3Z7l4Y/giphy.gif?cid=ecf05e47ndfufidlb230ur290z47nticuectuxtpza2hqpwt&ep=v1_gifs_search&rid=giphy.gif&ct=g'>"
    elif guess < number:
        return f"<h1>The number is not {guess}</h1>" \
                "<img width='500' src='https://media0.giphy.com/media/LFA6Qbj3Z7l4Y/giphy.gif?cid=ecf05e47ndfufidlb230ur290z47nticuectuxtpza2hqpwt&ep=v1_gifs_search&rid=giphy.gif&ct=g'>"
    else:
         return f"<h1>You got it right! The number is {number}</h1>" \
                "<img width='500' src='https://media2.giphy.com/media/ohMtDzrhrWgnK/giphy.gif?cid=ecf05e47irtyvffrhv73udm8jy183o34ehxxtbl33crwsn4i&ep=v1_gifs_search&rid=giphy.gif&ct=g'>"

if __name__ == "__main__":
    app.run(debug=True)