from datetime import datetime
import re


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

    def validate_license_plate_format(self, license_plate):
        license_plate_pattern = re.compile('[A-Z]{3,3}-[0-9]{3,4}')

        if license_plate_pattern.match(license_plate) is None:
            return False
        else:
            return True
