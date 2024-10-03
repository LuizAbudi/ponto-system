from models.sheet_data import SheetData
from datetime import datetime, timedelta


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

    def adjust_times(self, rows):
        total_seconds_added = 0

        for i in range(1, len(rows)):
            previous_end_time = datetime.strptime(
                rows[i-1].hora_fim_formatada, '%d/%m/%Y %H:%M:%S')
            current_start_time = datetime.strptime(
                rows[i].hora_inicio_formatada, '%d/%m/%Y %H:%M:%S')

            if current_start_time <= previous_end_time:
                new_start_time = previous_end_time + timedelta(seconds=1)
                rows[i].hora_inicio_formatada = new_start_time.strftime(
                    '%d/%m/%Y %H:%M:%S')
                rows[i].hora_inicio = new_start_time.strftime('%H:%M')
                total_seconds_added += 1

        if rows:
            last_task_end_time = datetime.strptime(
                rows[-1].hora_fim_formatada, '%d/%m/%Y %H:%M:%S')
            new_end_time = last_task_end_time + \
                timedelta(seconds=total_seconds_added)
            rows[-1].hora_fim_formatada = new_end_time.strftime(
                '%d/%m/%Y %H:%M:%S')
            rows[-1].hora_fim = new_end_time.strftime('%H:%M')

        return rows

    def format_rows(self, rows):
        formatted_rows = []
        for row in rows:
            formatted_rows.append(
                f"Data: {row.data}\n"
                f"Descrição: {row.descricao}\n"
                f"Hora Início: {row.hora_inicio}\n"
                f"Hora Fim: {row.hora_fim}\n"
                f"Hora Início Formatada: {row.hora_inicio_formatada}\n"
                f"Hora Fim Formatada: {row.hora_fim_formatada}\n"
                "--------------------------------------\n"
            )
        return "\n".join(formatted_rows)

    def convert_to_entries(self, rows):
        entries = []
        for row in rows:
            entry = {
                'task': row.tarefa,
                'dh_inicio': row.hora_inicio_formatada,
                'dh_fim': row.hora_fim_formatada,
                'descricao': row.descricao
            }
            entries.append(entry)
        return entries
