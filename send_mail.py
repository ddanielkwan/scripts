import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication

#login credentials
sender = 'xx' 
receiver  = 'xx'
msg = 'Placeholder Msg'
username = 'xx'
password = 'xx'

msg = MIMEMultipart()
msg['Subject'] = 'Placeholder Subject'
msg['From'] = sender
msg['To'] = receiver

#msg body
msgText = MIMEText('Msg', 'html')
msg.attach(msgText)

#attach files
ics_file = MIMEApplication(open("invite.ics", 'rb').read())
ics_file.add_header('Content-Disposition', 'attachment', filename= "invite.ics")
msg.attach(ics_file)

#connect 
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(sender, receiver, msg.as_string())
server.quit()