from datetime import datetime


class Validator:
    def validate_date_format(self, str_date):
        try:
            datetime.strptime(str_date, "%d/%m/%Y")
            return True
        except ValueError:
            return False
