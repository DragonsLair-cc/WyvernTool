from core.command import Command

class InstallCommand(Command):
    def __init__(self, install_command: str):
        super().__init__()
        self.install_command = install_command.split()

    def main_command(self):
        package_set = set()
        for packages in self.selected.values():
            for item in packages:
                package_set.add(item)
        return [self.install_command + sorted(package_set)]