from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class Sheets:

    # If modifying these scopes, delete the file token.json.
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    # The ID and range of a sample spreadsheet.
    SPREADSHEET_ID = '1rKIjFna5fHVpXyJ8i6J6CnYSnpFEYjExmrGnfw7hdZs'
    RANGE_NAME = 'leads!A:Z'
    
    
    def __init__(self) -> None:
        
        self.creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.json'):
            self.creds = Credentials.from_authorized_user_file('token.json', self.SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'backend\gsheets_key.json', self.SCOPES)
                self.creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(self.creds.to_json())

        self.service = build('sheets', 'v4', credentials=self.creds)

        # Call the Sheets API
        self.sheet = self.service.spreadsheets()
        self.result = self.sheet.values().get(spreadsheetId=self.SPREADSHEET_ID,
                                    range=self.RANGE_NAME).execute()
        self.values = self.result.get('values', [])
            
    
    def inserir_dado(self, dado: list) -> dict:
        print(dado)
        numero_da_linha = len(self.values)+1
        self.result = self.sheet.values().update(
            spreadsheetId=self.SPREADSHEET_ID,
            range=f'leads!A{numero_da_linha}',
            valueInputOption="USER_ENTERED",
            body={"values":dado}
        ).execute()
        


if __name__ == '__main__':
    Sheets()
