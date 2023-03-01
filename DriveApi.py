from Google import Create_Service
from googleapiclient.http import MediaFileUpload
from pathlib import Path
CLIENT_SECRET_FILE = 'client_secret_GoogleCloudDemo.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']



folderID = '130xfcgv1TKzCoKXKe9umY1tB_vxtj9ko'
service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
mimeType = 'application/pdf'
def uploadFile(users):
    for user in users:
        file_metadata = {
            'name': user.fileName,
            'parents': [folderID]
        }
        media = MediaFileUpload(str(Path.home())+'/Downloads/{0}'.format(user.fileName), mimetype= mimeType)
        service.files().create(
            body=file_metadata,
            media_body = media,
            fields = 'id'
        ).execute() 
def retrieveLink(teams):
    files = []
    for team in teams:
        for member in team.members:
            fileName = member.fileName
            query = f"'{folderID}' in parents and name = '{fileName}'"
            results = service.files().list(q=query, fields="files(id, name)").execute()
            items = results.get('files', [])

            if not items:
                print('File not found in the folder.' + member.name + "THIS IS THE FILENAME: "+fileName)
            else:
                file_id = items[0]['id']
                file_link = f'https://drive.google.com/file/d/{file_id}'
                files.append(file_link)
                print(f'File link: {file_link}')

    return files
        
