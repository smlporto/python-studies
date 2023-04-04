import requests
import smtplib
from datetime import datetime
import time


MY_EMAIL = "email"
MY_PASSWORD = "password"
SJK_LAT = -23.1867782
SJK_LNG = -45.8854538


def is_iss_overhead():
    response = requests.get("https://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if SJK_LAT - 5 <= iss_latitude <= SJK_LAT + 5 and SJK_LNG - 5 <= iss_longitude <= SJK_LNG + 5:
        return True


def is_night():
    parameters = {
        "lat": SJK_LAT,
        "lng": SJK_LNG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    data = response.json()
    sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
    sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

    time_now = datetime.now()

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up\n\nThe ISS is above you in the sky!."
        )
