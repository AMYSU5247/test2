import smtplib, ssl
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.base import MIMEBase
from email import encoders

sender = "thetherafans@gmail.com"
receiver = ["thetherafans520@gmail.com","minnie243554@gmail.com"]
password = "lhrx mtgh qzhd qszq"
for i in receiver:
    msg = MIMEMultipart()
    msg["From"]= sender
    msg["TO"]= i
    msg["Subject"]=Header("Test send email","utf-8").encode()

    body="This is send by python"

    msg_text=MIMEText(body)
    msg.attach(msg_text)

    text_path = "test.txt"
    with open (text_path,"r") as f:
       part =MIMEBase("application","octet-stream")
       part.set_payload(f.read())
       encoders.encode_base64(part)
       part.add_header('Content-Disposition','attachment; filename="test.txt"')
       msg.attach(part)

    c= ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=c) as server:
      server.login(sender,password)
      server.sendmail(sender,receiver,msg.as_string())
print("succes send mail")





