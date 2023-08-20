import datetime

from src.schedule import ScheduleTime
from src.schedule import Holiday


class Predictor:
    def return_last_digit(self, license_plate):
        return int(license_plate[-1])

    def predict(self, str_time):
        time = datetime.datetime.strptime(str_time, "%H:%M").time()
        if (ScheduleTime.TIME_MORNING_START.value <= time <= ScheduleTime.TIME_MORNING_END.value or
                ScheduleTime.TIME_AFTERNOON_START.value <= time <= ScheduleTime.TIME_AFTERNOON_END.value):
            return False
        return True

    def predict_according_to_date(self, license_plate, str_date):
        last_digit = self.return_last_digit(license_plate)
        date = datetime.datetime.strptime(str_date, "%d/%m/%Y").date()
        week_day = date.weekday()
        # It verifies if the date is a holiday
        for holiday in Holiday:
            if date == holiday.value:
                return True

        if week_day == 0:
            if 1 <= last_digit <= 2:
                return False
        elif week_day == 1:
            if 3 <= last_digit <= 4:
                return False
        elif week_day == 2:
            if 5 <= last_digit <= 6:
                return False
        elif week_day == 3:
            if 7 <= last_digit <= 8:
                return False
        elif week_day == 4:
            if last_digit == 9 or last_digit == 0:
                return False
        return True
