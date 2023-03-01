from Google import Create_Service
import base64
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.message import EmailMessage
import mimetypes
from pathlib import Path

CLIENT_SECRET_FILE = 'client_secret_GoogleCloudDemo.json'
API_NAME = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)


def sendEmail(teams, files):
    count = 0
    print(files)
    for team in teams:
        email = ""
        message = ""
        for member in team.members:
            email += member.email+","
            message += member.name+":"+files[count]+"\n"
            count += 1
        email = email[:-1]
        print(email)
        EmailMessage = message
        mimeMessage = MIMEMultipart()
        mimeMessage['to'] = email
        mimeMessage['subject'] = f"CAD Designathon 2023 - ({team.name}) Certificates"
        mimeMessage.attach(MIMEText(EmailMessage, 'plain'))

        # encoded message
        encoded_message = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

        create_message = {
            'message': {
                'raw': encoded_message
            }
        }
        # pylint: disable=E1101
        draft = service.users().drafts().create(userId="me", body=create_message).execute()
    # for user in peoples:
    #     EmailMessage = "Dear "+user.name+"\n\nCongrats on doing the thing. See you next year!\nHere is your certificate link:"+ files[count]+ "\n\n  Sincerely, MDL PEOPLE"
    #     mimeMessage = MIMEMultipart()
    #     mimeMessage['to'] = user.email
    #     mimeMessage['subject'] = "MDL Designathon Participant Certificates"
    #     mimeMessage.attach(MIMEText(EmailMessage, 'plain'))

    #     # encoded message
    #     encoded_message = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

    #     create_message = {
    #         'message': {
    #             'raw': encoded_message
    #         }
    #     }
    #     # pylint: disable=E1101
    #     draft = service.users().drafts().create(userId="me", body=create_message).execute()
    #     count += 1

