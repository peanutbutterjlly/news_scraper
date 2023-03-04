import smtplib
from email.message import EmailMessage

from decouple import config


def send_news() -> None:
    """send news summary to myself via email; contents come from summary.txt"""

    print("sending news summary")
    SENDER = config("EMAIL_HOST_USER")
    RECEIVER = config("EMAIL_HOST_USER")
    SUBJECT = "News Summary"
    BODY = open("summary.txt", "r").read()

    MESSAGE = EmailMessage()
    MESSAGE.set_content(BODY)
    MESSAGE["Subject"] = SUBJECT
    MESSAGE["From"] = SENDER
    MESSAGE["To"] = RECEIVER

    SMTP_SERVER = config("EMAIL_HOST")
    SMTP_PORT = config("EMAIL_PORT")
    USERNAME = config("EMAIL_HOST_USER")
    PASSWORD = config("EMAIL_HOST_PASSWORD")

    SMTP_OBJ = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    SMTP_OBJ.ehlo()
    SMTP_OBJ.starttls()
    SMTP_OBJ.login(USERNAME, PASSWORD)

    SMTP_OBJ.send_message(MESSAGE)

    SMTP_OBJ.quit()
    print("news summary sent")


if __name__ == "__main__":
    send_news()
