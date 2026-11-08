import subprocess
from core.status import CommandStatus

class Command:
    def __init__(self):
        self.selected = {}
        self.status = CommandStatus.IDLE

    def toggle(self, name:str, value:str, checked:bool):
        if checked and name not in self.selected:
            self.selected[name] = value
        elif not checked and name in self.selected:
            self.selected.pop(name)

    def build_command(self):
        raise NotImplementedError()

    def execute(self):
        if not self.selected:
            return
        if self.status == CommandStatus.RUNNING:
            return
        self.status = CommandStatus.RUNNING
        print("Running")
        try:
            subprocess.run(self.build_command(), shell=True)
            self.status = CommandStatus.COMPLETED
        except subprocess.CalledProcessError as e:
            self.status = CommandStatus.ERROR
            print(e)