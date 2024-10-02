from models.sheet_data import SheetData

class SheetService:
    def __init__(self, sheet_repository):
        self.sheet_repository = sheet_repository
        
    def get_range_names(self, spreadsheet_id):
        return self.sheet_repository.get_range_names(spreadsheet_id)
        
    def get_all_rows(self, spreadsheet_id, range_name):
        rows = self.sheet_repository.get_sheet_data(spreadsheet_id, range_name)
        return [SheetData(row) for row in rows]
    
    def print_all_rows(self, rows):
        for row in rows:
            print(row)
    
    def filter_valid_rows(self, rows):
        return [row for row in rows if row.descricao != '' and row.apontado == 'FALSE']
    
        
    
