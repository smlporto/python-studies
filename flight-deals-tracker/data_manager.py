import requests
from config import *

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']


SPREADSHEET_ID = '1V-NkFJhiI7J79B9RYzSARXrg8T_tv8rr72uktXBI44Q'
RANGE_NAME = 'prices!A1:C11'

class DataManager:

    def __init__(self):
        self.creds = None
        self.login()
        self.destiny_info = {}
        
    def login(self):
        if os.path.exists('token.json'):
            self.creds = Credentials.from_authorized_user_file('token.json', SCOPES)

        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                self.creds = flow.run_local_server(port=0)

            with open('token.json', 'w') as token:
                token.write(self.creds.to_json())
        
    def get_data(self):
        service = build('sheets', 'v4', credentials=self.creds)

        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
        self.destiny_info = result["values"]
        return self.destiny_info
        
        
    def update_data(self):
        service = build('sheets', 'v4', credentials=self.creds)

        sheet = service.spreadsheets()
        new_info = [
            ["IATA Code"],
        ]
        
        for i, city in enumerate(self.destiny_info):
            if i > 0:
                code = city[1]
                new_info.append([code])
                
        result = sheet.values().update(spreadsheetId=SPREADSHEET_ID, range="B1", valueInputOption="USER_ENTERED", body={'values': new_info}).execute()
        