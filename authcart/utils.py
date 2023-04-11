import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

shop_name = "Cole's Store"
confirm_code = 123456
sender_email = 'anhttse06009@gmail.com'
sender_password = 'amcevyjoatufwqim'
smtp_server = 'smtp.gmail.com'
smtp_port = 587


def send_email(email):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = email
    msg['Subject'] = f'{shop_name } Confirmation Code: {confirm_code}'
    msg.attach(MIMEText("test message",'plain'))
    server = smtplib.SMTP(smtp_server,smtp_port)
    server.starttls()

    server.login(sender_email,sender_password)
    text = msg.as_string()
    server.sendmail(sender_email, email,text)
    server.quit()
