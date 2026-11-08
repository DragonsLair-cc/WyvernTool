from gi.repository import Adw

class SystemTweaksView(Adw.PreferencesPage):
    def __init__(self, tweak_command, tweaks:dict):
        super().__init__()
        self.tweak_command = tweak_command
        self.tweaks = tweaks

        for category, packages_list in self.tweaks.items():
            group = Adw.PreferencesGroup(title=category)
            self.add(group)

            for name, packages in packages_list.items():
                row = Adw.SwitchRow(title=name)
                row.connect("notify::active", self.tweak_toggle, name, packages)
                group.add(row)

    def tweak_toggle(self, row, _param, name, packages):
        self.tweak_command.toggle(name, packages, row.get_active())