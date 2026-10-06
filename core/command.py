import subprocess
from core.status import CommandStatus

class Command:
    def __init__(self):
        self.selected = {}
        self.status = CommandStatus.PENDING

    def toggle(self, name:str, value, checked: bool):
        if checked and name not in self.selected:
            self.selected[name] = value
        elif not checked and name in self.selected:
            self.selected.pop(name)

    def build_command(self):
        raise NotImplementedError("Commands are implemented by subclasses")

    def run(self):
        if not self.selected:
            return
        if self.status == CommandStatus.RUNNING:
            return
        self.status = CommandStatus.RUNNING
        try:
            subprocess.run(self.build_command(), check=True)
            self.status = CommandStatus.COMPLETE
            print(f"Operation: {self.status.name}")
        except Exception as e:
            self.status = CommandStatus.ERROR
            print(e)