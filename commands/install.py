from core.command import Command

class InstallCommand(Command):
    def __init__(self, install_command: str):
        super().__init__()
        self.install_command = install_command

    def build_command(self):
        package_string = ""
        for packages in self.selected.values():
           for item in packages:
               package_string += " " + item
        return ["pkexec", "sh", "-c", self.install_command + package_string]