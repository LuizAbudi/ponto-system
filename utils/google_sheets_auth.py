import os
from google.oauth2.service_account import Credentials


class GoogleSheetsAuth:
    @staticmethod
    def get_credentials():
        scopes = ['https://www.googleapis.com/auth/spreadsheets.readonly']
        creds = Credentials.from_service_account_file(
            os.getenv("GOOGLE_APPLICATION_CREDENTIALS"), scopes=scopes)
        return creds
