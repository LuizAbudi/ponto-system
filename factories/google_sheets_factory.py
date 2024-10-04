from repositories.google_sheets_repository import GoogleSheetsRepository
from utils.google_sheets_auth import GoogleSheetsAuth


class GoogleSheetsFactory:
    @staticmethod
    def create_sheets_repository():
        credentials = GoogleSheetsAuth.get_credentials()
        return GoogleSheetsRepository(credentials)
