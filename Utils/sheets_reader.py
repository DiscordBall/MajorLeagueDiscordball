import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']


def get_creds():
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
    return creds


def get_service_sheets():
    service = build('sheets', 'v4', credentials=get_creds()).spreadsheets().values()
    return service


def read_sheet(spreadsheet_id, page_name):
    service = get_service_sheets()
    return service.get(spreadsheetId=spreadsheet_id, range=page_name).execute().get('values', [])


def append_sheet(spreadsheet_id, page_name, data):
    get_service_sheets().append(spreadsheetId=spreadsheet_id,
                                range=page_name,
                                valueInputOption='USER_ENTERED',
                                insertDataOption='INSERT_ROWS',
                                body={"values": [list(data)]}
                                ).execute()


def batch_update(spreadsheet_id, page_name, data):
    data = [
        {
            'range': page_name,
            'values': data
        },
        # Additional ranges to update ...
    ]
    body = {
        'valueInputOption': 'USER_ENTERED',
        'data': data
    }

    get_service_sheets().batchUpdate(spreadsheetId=spreadsheet_id, body=body).execute()


def clear_page(spreadsheet_id, page_name):
    service = get_service_sheets()
    service.clear(spreadsheetId=spreadsheet_id, range=page_name, body={}).execute()
