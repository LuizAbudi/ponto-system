from factories.google_sheets_factory import GoogleSheetsFactory
from services.sheet_service import SheetService
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "config/credentials.json"


def main():
    spreadsheet_id = '10h3eIZNGBuOKVYesywxtDwEbdTF76fqt2ckZF-9pTw8'
    
    sheet_repository = GoogleSheetsFactory.create_sheets_repository()

    sheet_service = SheetService(sheet_repository)
    
    all_range_names = sheet_service.get_range_names(spreadsheet_id)
    last_range_name = all_range_names[-1]    

    rows = sheet_service.get_all_rows(spreadsheet_id, last_range_name)
    
    filtered_rows = sheet_service.filter_valid_rows(rows)
    print(filtered_rows)

if __name__ == '__main__':
    main()
