from datetime import datetime
import pandas as pd
import smtplib
import random

SENDER = "..."
PASSWORD = "..."

def get_month_day():
    today = datetime.now()
    return today.month, today.day

def send_mail(email, letter):
    with smtplib.SMTP("smtp.gmail.com") as con:
        con.starttls()
        con.login(user=SENDER, password=PASSWORD)
        con.sendmail(
            from_addr=SENDER,
            to_addrs=email,
            msg=f"Subject: Happy Birthday!\n\n{letter}"
        )

def select_letter(name):
    num = random.randint(1,3)
    with open(f"letter_templates/letter_{num}.txt") as f:
        letter = f.read().replace("[NAME]", name)
    return letter

def main():
    df = pd.read_csv("birthdays.csv")
    month, day = get_month_day()
    for _, row in df.iterrows():
        if row["month"] == month and row["day"] == day:
            letter = select_letter(row["name"])
            send_mail(row["email"], letter)

main()