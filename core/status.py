from enum import Enum

class CommandStatus(Enum):
    PENDING = 0
    RUNNING = 1
    COMPLETE = 2
    ERROR = 3