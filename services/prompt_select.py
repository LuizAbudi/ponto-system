from InquirerPy import prompt


class PromptSelect:
    def __init__(self, range_names):
        self.range_names = range_names
        print("PromptSelect", self.range_names)

    def select_month(self):
        questions = [
            {
                "type": "list",
                "name": "selected_month",
                "message": "Selecione o mês para o apontamento:",
                "choices": self.range_names
            }
        ]

        answers = prompt(questions)
        selected_month = answers['selected_month']
        print(f"Mês selecionado: {selected_month}")
        return selected_month
