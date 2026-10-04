from gi.repository import Adw

class InstallView(Adw.PreferencesPage):
    def __init__(self, install_native, install_flatpak, native_programs, flatpak_programs):
        super().__init__()
        self.install_native = install_native
        self.install_flatpak = install_flatpak

        for category, packages_dict in native_programs.items():
            group = Adw.PreferencesGroup(title = category)
            self.add(group)

            for name, packages in packages_dict.items():
                row = Adw.SwitchRow(title = name)
                row.connect("notify::active", self.native_on_toggled, name, packages)
                group.add(row)

        group = Adw.PreferencesGroup(title = "Flatpak Packages")
        self.add(group)

        for name, packages in flatpak_programs.items():
            row = Adw.SwitchRow(title = name)
            row.connect("notify::active", self.flatpak_on_toggled, name, packages)
            group.add(row)


    def native_on_toggled(self, row, _param, name, packages):
        self.install_native.toggle(name, packages, row.get_active())

    def flatpak_on_toggled(self, row, _param, name, packages):
        self.install_flatpak.toggle(name, packages, row.get_active())