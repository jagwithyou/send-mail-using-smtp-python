from email.mime.base import MIMEBase 
from email import encoders 

def add_attachment(msg, file_name_with_path):
    ''' Add attachment to the message instance of MIMEMultipart.
     Takes MIMEMultipart instance and attachment file path as parameter and returns MIMEMultipart instance 
    '''
    # Open the file to be sent 
    filename = file_name_with_path.split("\\")[-1]
    attachment_file = open(file_name_with_path, "rb") 

    # Instance of MIMEBase and named as attachment
    attachment = MIMEBase('application', 'octet-stream') 

    # To change the payload into encoded form 
    attachment.set_payload((attachment_file).read()) 

    # Encode into base64 
    encoders.encode_base64(attachment) 

    #Add header to the attachment
    attachment.add_header('Content-Disposition', "attachment; filename= %s" % filename) 

    # Attach the instance 'p' to instance 'msg' 
    msg.attach(attachment) 
    return msg

if __name__ == '__main__':
    #importing for testing
    from send_mail import *
    import smtp_server_config as config

    receiver_mail = config.RECEIVER_EMAIL
    print(receiver_mail)
    subject = 'Python email'
    message = "Python Test Mail"
    attachments = ['price.xlsx']
    send_mail(receiver_mail, subject, message, attachments)