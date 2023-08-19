from enum import Enum
from datetime import time


class ScheduleTime(Enum):
    TIME_MORNING_START = time(7, 00)
    TIME_MORNING_END = time(9, 30)
    TIME_AFTERNOON_START = time(16, 00)
    TIME_AFTERNOON_END = time(19, 30)
