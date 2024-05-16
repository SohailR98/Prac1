import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from_addr = 'sohailrr@gmail.com'

data = pd.read_csv(r"C:\Users\User\Desktop\mail_id.csv")
to_addr = data['email'].tolist()
name = data['name'].tolist()

l = len(name)
email = "sohailrr@gmail.com"
password = "mizv jypv uuni zsqj"

for i in range(1):
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr[i]
    msg['Subject'] = 'Test Subject'

    body = name[i]+'meddsgr ksmdjhnc'

    msg.attach(MIMEText(body, 'plain'))
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login(email, password)
    text = msg.as_string()
    mail.sendmail(from_addr, to_addr[i], text)
    print("mail sent")
    mail.quit()


# Second factor authentication is required for sending mail
# mizv jypv uuni zsqj password for app mail
