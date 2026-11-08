from enum import Enum

class CommandStatus(Enum):
    IDLE = 0
    RUNNING = 1
    COMPLETED = 2
    ERROR = 3