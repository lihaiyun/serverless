import json
import os
from googleapiclient.discovery import build
from google.oauth2 import service_account
import re

# Path to your credentials file
SERVICE_ACCOUNT_FILE = os.path.join(os.path.dirname(__file__), '../credentials.json')

# Scopes required for accessing Google Sheets
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

def get_sheet_name(spreadsheet_id):
    # Authenticate and create the service object
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API to get the spreadsheet metadata
    sheet_metadata = service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()
    
    # Get the sheet name from metadata
    sheet_title = sheet_metadata.get('properties', {}).get('title', 'No Title Found')
    return sheet_title

def extract_spreadsheet_id_from_url(url):
    # Extract spreadsheet ID from the URL
    match = re.search(r'/d/([a-zA-Z0-9-_]+)', url)
    if match:
        return match.group(1)
    return None

def handler(event, context):
    # Example public URL of the Google Sheet
    public_url = os.getenv('GOOGLE_SHEET_URL')

    spreadsheet_id = extract_spreadsheet_id_from_url(public_url)
    sheet_name = None
    if spreadsheet_id:
        sheet_name = get_sheet_name(spreadsheet_id)

    body = {
        "spreadsheet_url": public_url,
        "spreadsheet_id": spreadsheet_id,
        "spreadsheet_name": sheet_name
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
