from enum import Enum
from datetime import time
from datetime import date


class ScheduleTime(Enum):
    TIME_MORNING_START = time(7, 00)
    TIME_MORNING_END = time(9, 30)
    TIME_AFTERNOON_START = time(16, 00)
    TIME_AFTERNOON_END = time(19, 30)


class Holiday(Enum):
    NEW_YEAR = date(2023, 1, 2)
    CARNAVAL_1 = date(2023, 2, 20)
    CARNAVAL_2 = date(2023, 2, 21)
    GOOD_FRIDAY = date(2023, 4, 7)
    LABOR_DAY = date(2023, 5, 1)
    PICHINCHA_BATTLE = date(2023, 5, 26)
    FIRST_CRY_OF_INDEPENDENCE = date(2023, 8, 11)
    GUAYAQUIL_INDEPENDENCE = date(2023, 10, 9)
    DAY_OF_THE_DEAD = date(2023, 11, 2)
    CUENCA_INDEPENDENCE = date(2023, 11, 3)
    QUITO_FOUNDATION = date(2023, 12, 4)
    CHRISTMAS = date(2023, 12, 25)


WEEK_DAYS = {
    0: {'last_digit': [1, 2]},
    1: {'last_digit': [3, 4]},
    2: {'last_digit': [5, 6]},
    3: {'last_digit': [7, 8]},
    4: {'last_digit': [9, 0]}
}

WEEKEND = [5, 6]
