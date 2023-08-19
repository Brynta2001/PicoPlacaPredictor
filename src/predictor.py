import datetime

from src.schedule import ScheduleTime


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
        pass
