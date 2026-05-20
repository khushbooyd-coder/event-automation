import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_venue_email(
    sender_email,
    app_password,
    receiver_email,
    subject,
    body
):

    try:

        msg = MIMEMultipart()

        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Subject"] = subject

        msg.attach(
            MIMEText(body, "plain")
        )

        server = smtplib.SMTP(
            "smtp.gmail.com",
            587
        )

        server.starttls()

        server.login(
            sender_email,
            app_password
        )

        server.send_message(msg)

        server.quit()

        return {
            "status": "sent"
        }

    except Exception as e:

        return {
            "status": "failed",
            "error": str(e)
        }

