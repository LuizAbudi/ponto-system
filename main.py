import os

from dotenv import load_dotenv

from factories.google_sheets_factory import GoogleSheetsFactory
from services.prompt_select import PromptSelect
from services.sheet_service import SheetService
from services.site_interaction import SiteInteraction
from utils.select_actual_month import SelectActualMonth

load_dotenv()

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "config/credentials.json"


def main():
    # Carregar variáveis de ambiente
    spreadsheet_id = os.getenv("GOOGLE_SPREADSHEET_ID")
    user = os.getenv("TASK_USER")
    password = os.getenv("TASK_PASSWORD")
    site_url = os.getenv("TASK_URL")
    chrome_path = os.getenv("CHROME_PATH")

    sheet_repository = GoogleSheetsFactory.create_sheets_repository()
    sheet_service = SheetService(sheet_repository)

    # Obter o mês do apontamento
    all_range_names = sheet_service.get_range_names(spreadsheet_id)
    filtered_range_names = SelectActualMonth(
        all_range_names).filter_actual_months()

    actual_month = PromptSelect(filtered_range_names).select_month()

    entries = sheet_service.get_entries_for_current_month(
        spreadsheet_id, actual_month)

    # Acessar o site e realizar o apontamento
    site_interaction = SiteInteraction(chrome_path)
    site_interaction.execute(site_url, user, password, entries)


if __name__ == '__main__':
    main()
