from datetime import datetime

from src.schedule import ScheduleTime, WEEKEND
from src.schedule import Holiday
from src.schedule import WEEK_DAYS


class Predictor:
    def return_last_digit(self, license_plate):
        return int(license_plate[-1])

    def is_holiday(self, date):
        for holiday in Holiday:
            if date == holiday.value:
                return True
        return False

    def is_in_time_range(self, time):
        if (ScheduleTime.TIME_MORNING_START.value <= time <= ScheduleTime.TIME_MORNING_END.value or
                ScheduleTime.TIME_AFTERNOON_START.value <= time <= ScheduleTime.TIME_AFTERNOON_END.value):
            return False
        return True

    def predict(self, license_plate, str_date, str_time):
        last_digit = self.return_last_digit(license_plate)
        time = datetime.strptime(str_time, "%H:%M").time()
        date = datetime.strptime(str_date, "%d/%m/%Y").date()
        week_day_date = date.weekday()

        # It verifies if the date is holiday or weekend
        if self.is_holiday(date) or week_day_date in WEEKEND:
            return True

        for WEEK_DAY in WEEK_DAYS:
            if week_day_date == WEEK_DAY:
                if last_digit in WEEK_DAYS[WEEK_DAY]['last_digit']:
                    if self.is_in_time_range(time):
                        return False
                    return True
                return True
