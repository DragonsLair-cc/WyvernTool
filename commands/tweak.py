from core.command import Command

class TweakCommand(Command):
    def __init__(self):
        super().__init__()

    def build_command(self):
        tweak_list = []
        for tweaks in self.selected.values():
            for tweak in tweaks:
                tweak_list.append(tweak)
            chained_command = " && ".join(tweak_list)
        return ["pkexec", "sh", "-c", chained_command]