from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTPException



# import ssl
# context = ssl.SSLContext(ssl.PROTOCOL_TLS)
import smtplib
MY_ADDRESS = "mknnotifyer@gmail.com"
MY_PASSWORD = "uxluuqehymoyqjnx"

def send_email(project_title,section_title,notification_title,description,deadline,email):
    try:
        s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        s.ehlo()
        s.login(MY_ADDRESS, MY_PASSWORD)
    except:
        print ('Something went wrong...')
    msg = MIMEMultipart()
    msg['From']=MY_ADDRESS
    msg['To']=email
    msg['Subject']=notification_title + " / " + section_title 
    msg.attach(MIMEText("(Проект: " + project_title + ")\n" + description, 'plain'))
    try:
        s.send_message(msg)
    
    except SMTPException as e:                             
        print("error error: " , e)

    del msg


# now = datetime.datetime.now()
# for i in range(5):
#     send_email("1","2","3","desc", "d", "h34th3n777@gmail.com")
# print (datetime.datetime.now() - now )