from enum import Enum

class StatusCode(Enum):
    SUCCESS = 1
    INIT_ERROR = 2
    COMMAND_ERROR = 3
    FAILED = 4
    RUNNING = 5

