class SheetData:
    def __init__(self, row: list):
        if len(row) < 9:
            row += [''] * (9 - len(row))

        self.data = row[0]
        self.tarefa = row[1]
        self.descricao = row[2]
        self.hora_inicio = row[3]
        self.hora_fim = row[4]
        self.total_horas = row[5]
        self.apontado = row[6]
        self.hora_inicio_formatada = row[7]
        self.hora_fim_formatada = row[8]

    def __repr__(self):
        return (f"Data: {self.data}\n"
                f"Codico Tarefa Task: {self.tarefa}\n"
                f"Descrição: {self.descricao}\n"
                f"Hora Início: {self.hora_inicio}\n"
                f"Hora Fim: {self.hora_fim}\n"
                f"Total de Horas: {self.total_horas}\n"
                f"Apontado: {self.apontado}\n"
                f"Hora Início Formatada: {self.hora_inicio_formatada}\n"
                f"Hora Fim Formatada: {self.hora_fim_formatada}")
