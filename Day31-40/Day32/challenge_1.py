import datetime as dt
import random
import smtplib

SENDER = "test@gmail.com"
RECEIVER = "test2@gmail.com"
PASSWORD = "test"

def get_body():
    now = dt.datetime.now()
    day_of_the_week = now.weekday()
    if day_of_the_week == 2:
        with open("quotes.txt") as f:
            quotes = f.readlines()
        return random.choice(quotes)

def send_email(quote):
    with smtplib.SMTP("smtp.gmail.com") as con:
        con.starttls()
        con.login(user=SENDER, password=PASSWORD)
        con.sendmail(
            from_addr=SENDER,
            to_addrs=RECEIVER,
            msg=f"Subject: Daily Motivation\n\n{quote}"
        )

send_email(get_body())
