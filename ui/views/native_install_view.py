from gi.repository import Adw

class NativeInstallView(Adw.PreferencesPage):
    def __init__(self, native_command, native_packages:dict):
        super().__init__()
        self.native_command = native_command
        self.native_packages = native_packages

        for category, packages_list in self.native_packages.items():
            group = Adw.PreferencesGroup(title=category)
            self.add(group)

            for name, packages in packages_list.items():
                row = Adw.SwitchRow(title=name)
                row.connect("notify::active", self.native_toggle, name, packages)
                group.add(row)

    def native_toggle(self, row, _param, name, packages):
        self.native_command.toggle(name, packages, row.get_active())