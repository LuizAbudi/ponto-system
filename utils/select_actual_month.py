from datetime import datetime


class SelectActualMonth:
    def __init__(self, all_range_names):
        self.all_range_names = all_range_names

    def actual_year(self):
        current_year = datetime.now().year
        return current_year

    def filter_actual_months(self):
        current_year = self.actual_year()
        filtered_range_names = [
            month for month in self.all_range_names if str(current_year) in month]
        return filtered_range_names
