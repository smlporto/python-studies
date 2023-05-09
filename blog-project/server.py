from flask import Flask, render_template
from datetime import datetime
import requests

app = Flask(__name__)

@app.route("/")
def home():
    current_year = datetime.now().year
    return render_template('index.html', year=current_year)

@app.route("/guess/<name>")
def guess(name):
    response_age = requests.get(f"https://api.agify.io?name={name}")
    response_gender = requests.get(f"https://api.genderize.io?name={name}")
    
    age_data = response_age.json()
    gender_data = response_gender.json()
    
    name_age = age_data["age"]
    name_gender = gender_data["gender"]
    return render_template('guess.html', name=name, age=name_age, gender=name_gender)

if __name__ == "__main__":
    app.run(debug=True)