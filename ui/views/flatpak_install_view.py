from gi.repository import Adw

class FlatpakInstallView(Adw.PreferencesPage):
    def __init__(self, flatpak_command, flatpak_packages:dict):
        super().__init__()
        self.flatpak_command = flatpak_command
        self.flatpak_packages = flatpak_packages

        for category, packages_list in self.flatpak_packages.items():
            group = Adw.PreferencesGroup(title=category)
            self.add(group)

            for name, packages in packages_list.items():
                row = Adw.SwitchRow(title=name)
                row.connect("notify::active", self.flatpak_toggle, name, packages)
                group.add(row)

    def flatpak_toggle(self, row, _param, name, packages):
        self.flatpak_command.toggle(name, packages, row.get_active())