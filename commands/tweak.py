from core.command import Command

class TweakCommand(Command):
    def __init__(self):
        super().__init__()

    def build_command(self):
        tweak_list = ""
        for tweak in self.selected.values():
            if not tweak_list:
                tweak_list += f"{tweak}"
                continue
            tweak_list += f" && {tweak}"
        return f"pkexec sh -c '{tweak_list}'"