from googleapiclient.discovery import build

class GoogleSheetsRepository:
    def __init__(self, credentials):
        self.service = build('sheets', 'v4', credentials=credentials)
        
    def get_range_names(self, spreadsheet_id):
        spreadsheet = self.service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()
        
        range_names = []
        for sheet in spreadsheet.get('sheets', []):
            title = sheet.get('properties', {}).get('title', '')
            range_names.append(title)

        return range_names

    def get_sheet_data(self, spreadsheet_id, range_name):
        sheet = self.service.spreadsheets()
        result = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
        return result.get('values', [])
