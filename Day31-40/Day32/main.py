import smtplib

sender = "test@gmail.com"
receiver = "test2@gmail.com"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=sender,password="password")
    connection.sendmail(
        from_addr=sender,
        to_addrs=receiver,
        msg="Subject: Hello\n\n Hello in body"
    )
    connection.close()