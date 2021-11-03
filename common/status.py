from enum import Enum
from logging import ERROR

class StatusCode(Enum):
    SUCCESS = 1
    FAILED = 2
    RUNNING = 3
    ERROR = 4
    UNACTIVATED = 5
