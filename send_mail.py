import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 
import smtp_server_config as config
from add_attachment import *

def send_mail(receiver_mail, subject, message, attachments):
    ''' Send mail with subject, Body and attachments to the receivers mail id
    parameters:
    receiver_mail - mail id of the receiver
    subject - subject of the mail
    message - body of the mail
    attachments - list of attachments to be attached
    '''
    # Configuring the MIMEMultipart
    msg = MIMEMultipart()
    msg['From'] = config.USER_NAME
    msg['To'] = receiver_mail
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    #Adding the attachments if present
    for attachment in attachments:
        msg = add_attachment(msg, attachment)

    # Start a session
    session = smtplib.SMTP(config.HOST, config.PORT)

    # Start TLS for security 
    session.starttls() 
    
    # Authentication 
    session.login(config.USER_NAME, config.PASSWORD) 
    
    # send the message via the server
    session.send_message(msg)
    
    # Terminating the session 
    session.quit()

if __name__ == '__main__':
    receiver_mail = config.RECEIVER_EMAIL
    subject = 'Python email'
    message = "Python Test Mail"
    attachments = []
    send_mail(receiver_mail, subject, message, attachments)