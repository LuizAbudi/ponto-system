import os
from factories.google_sheets_factory import GoogleSheetsFactory
from services.sheet_service import SheetService
from services.site_interaction import SiteInteraction

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "config/credentials.json"


def main():
    spreadsheet_id = '10h3eIZNGBuOKVYesywxtDwEbdTF76fqt2ckZF-9pTw8'

    sheet_repository = GoogleSheetsFactory.create_sheets_repository()

    sheet_service = SheetService(sheet_repository)

    all_range_names = sheet_service.get_range_names(spreadsheet_id)
    last_range_name = all_range_names[-1]

    rows = sheet_service.get_all_rows(spreadsheet_id, last_range_name)

    valid_rows = sheet_service.filter_valid_rows(rows)

    adjusted_rows = sheet_service.adjust_times(valid_rows)

    entries = sheet_service.convert_to_entries(adjusted_rows)

    site_url = 'https://taskweb.db1group.com/#/taskico'

    site_interaction = SiteInteraction()
    site_interaction.access_site(site_url)
    site_interaction.login_in_site(site_url, 'LUIZ.ABUDI', '!@#Mudar')
    site_interaction.process_entries(entries)
    site_interaction.close()


if __name__ == '__main__':
    main()
