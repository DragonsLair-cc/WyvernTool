import subprocess
from core.status import CommandStatus

class Command:
    def __init__(self):
        self.selected = {}
        self.status = CommandStatus.PENDING

    def toggle(self, name:str, value, checked: bool):
        """Install commands use lists for value while tweaks use strings"""
        if checked and name not in self.selected:
            self.selected[name] = value
        elif not checked and name in self.selected:
            self.selected.pop(name)

    def main_command(self):
        raise NotImplementedError("Commands are implemented by their subclasses")

    def run(self):
        if not self.selected:
            return
        if self.status == CommandStatus.RUNNING:
            return
        self.status = CommandStatus.RUNNING
        try:
            for command in self.main_command():
                subprocess.run(command, check=True)
            self.status = CommandStatus.COMPLETE
        except Exception as e:
            self.status = CommandStatus.ERROR
            print(e)