import smtplib
from email.mime.text import MIMEText

def send_email(title: str, content, email: str):
    msg = MIMEText(content)
    msg["Subject"] = title
    msg["From"] = "email_you_created_in_brevosend.com" # Use the same email you sigined in with at brevosend.com to send the emails
    msg["To"] = email 

    with smtplib.SMTP("smtp-relay.brevo.com", 587) as server:
        server.starttls()
        server.login("login_email", "secert_password") # You will get these after signing in at brevosend.com
        server.send_message(msg)

send_email("Email Title!", "This is the email content body!", "the_reciever_email@their.domain")


