from core.command import Command

class InstallCommand(Command):
    def __init__(self, package_manager:str):
        super().__init__()
        self.package_manager = package_manager

    def build_command(self):
        package_list = ""
        for package in self.selected.values():
            package_list += f" {package}"
        return f"pkexec {self.package_manager}{package_list} -y"