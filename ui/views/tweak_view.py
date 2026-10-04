from gi.repository import Adw

class TweakView(Adw.PreferencesPage):
    def __init__(self, tweak_command, tweak_list):
        super().__init__()
        self.tweak_command = tweak_command
        self.tweak_list = tweak_list

        for name, tweaks in tweak_list.items():
            group = Adw.PreferencesGroup(title=name)
            self.add(group)

            for tweak_name, tweak in tweaks.items():
                row = Adw.SwitchRow(title=tweak_name)
                row.connect("notify::active", self.on_toggled, tweak_name, tweak)
                group.add(row)

    def on_toggled(self, row, _param, name, tweak):
        self.tweak_command.toggle(name, tweak, row.get_active())