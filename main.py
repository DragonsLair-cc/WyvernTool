import subprocess
from enum import Enum

class CommandStatus(Enum):
    PENDING = 0
    RUNNING = 1
    COMPLETE = 2
    ERROR = 3

class InstallCommand:
    def __init__(self, install_command):
        self.install_command = install_command.split()
        self.package_dictionary = {}
        self.status = CommandStatus.PENDING

    def toggle_package(self, package_name, package_list, checked):
        if not checked and package_name in self.package_dictionary:
            self.package_dictionary.pop(package_name)
        elif checked and package_name not in self.package_dictionary:
            self.package_dictionary[package_name] = package_list

    def install_package(self):
        if not self.package_dictionary:
            return
        elif self.status == CommandStatus.RUNNING:
            return
        self.status = CommandStatus.RUNNING
        package_set = set()
        for packages in self.package_dictionary.values():
            for item in packages:
                package_set.add(item)
        command = self.install_command + sorted(package_set)
        try:
            subprocess.run(command, check=True)
            self.status = CommandStatus.COMPLETE
        except Exception as e:
            print(e)
            self.status = CommandStatus.ERROR