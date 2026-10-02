from core.command import Command

class TweakCommand(Command):
    def __init__(self):
        super().__init__()

    def main_command(self):
        tweak_list = []
        for tweaks in self.selected.values():
            tweak_list.append(tweaks.split())
        return tweak_list