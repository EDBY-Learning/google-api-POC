from __future__ import print_function
import os.path
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from utils.sheet.append import append_values
from utils.sheet.populate import populate_values
from services import gmail, gsheet

SCOPES = ['https://www.googleapis.com/auth/drive.file','https://www.googleapis.com/auth/gmail.send']

def setup():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def main():

    creds = setup()
    sheet_service = gsheet.getSheetHandle(creds)
    spreadsheet_id = gsheet.getSheetId(sheet_service,"Log test")
    
    # result = append_values(sheet_service,spreadsheet_id,
    #         'Sheet1', 'USER_ENTERED', [
    #             ['A', 'B'],
    #             ['C', 'D']
    #         ])
    mail_service = gmail.getMailHandle(creds)
    TO = ""
    if TO:
        message = gmail.create_message(TO,'Test 1','Hello World')
        gmail.SendMessageInternal(mail_service,'me',message)
    else:
        raise ValueError("Set who are you sending mail")

if __name__ == '__main__':
    main()