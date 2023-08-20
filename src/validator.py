from datetime import datetime


class Validator:
    def validate_date_format(self, str_date):
        try:
            datetime.strptime(str_date, "%d/%m/%Y")
            return True
        except ValueError:
            return False

    def validate_time_format(self, str_time):
        try:
            datetime.strptime(str_time, "%H:%M")
            return True
        except ValueError:
            return False
