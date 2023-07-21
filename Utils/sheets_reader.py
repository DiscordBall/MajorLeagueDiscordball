import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']


def read_sheet(spreadsheet_id, page_name):
    creds = None
    if os.path.exists(f'{os.path.dirname(os.getcwd())}\\Utils\\token.pickle'):
        with open(f'{os.path.dirname(os.getcwd())}\\Utils\\token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(f'{os.path.dirname(os.getcwd())}\\Utils\\credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open(f'{os.path.dirname(os.getcwd())}\\Utils\\token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=spreadsheet_id, range=page_name).execute()
    values = result.get('values', [])
    return values
