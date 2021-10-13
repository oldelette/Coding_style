import email.message
import smtplib

msg = email.message.EmailMessage()

from_a = "leegavintest@gmail.com"
to_b = "ssp19960710@gmail.com"


msg["From"] = from_a
msg["To"] = to_b
msg["Subject"] = "Hello"

msg.add_alternative("<h3>HTML content</h3>Mail test", subtype="html")

# acc = input("Please input your gmail account: ")
# password = input("Please input your password")
acc = "leegavintest@gmail.com"
password = "asdf0710"

try:
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(acc, password)
    server.send_message(msg)
    print("Mail Send Successful")
except smtplib.SMTPException:
    print ("Error: Can't send the mail")

server.close()
