from string import Template
from get_contact_list import *
from send_mail import *

def read_template(filename):
    ''' Returns a Template object comprising the contents of the 
    file specified by filename.
    '''
    
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)



def send_mail_to_contact_list(contact_list_file_path, subject, message_template_path, attachments):
    ''' Send mail to all the contacts from the contact list file individually 
    with subject, message and attachments
    parameters:
    contact_list_file_path - the path of the contact list file, it can be a txt/xlsx/csv file
    subject - subject of the mail
    message_template_path - path of the message template file
    attachments - list of attachments to be attached
    '''
    contact_list = get_contact_list(contact_list_file_path)
    message_template = read_template(message_template_path)

    for name, email in contact_list:
        # add in the actual person name to the message template
        message = message_template.substitute(PERSON_NAME=name.title())
        send_mail(email, subject, message, attachments)
        print("message sent to : ", name)



if __name__ == '__main__':
    contact_list_file_path = '..\contact_list.xlsx'
    message_template_path = '..\message.txt'
    subject = 'Python email'
    attachments = ["..\price.xlsx", "..\message.txt"]
    send_mail_to_contact_list(contact_list_file_path, subject, message_template_path, attachments)