from gi.repository import Adw
from ui.main_window import MainWindow

class WyvernTool(Adw.Application):
    def __init__(self, native_command, flatpak_command, tweak_command, native_packages:dict, flatpak_packages:dict, tweaks:dict, service):
        super().__init__(application_id="io.github.wyvern.WyvernTool")
        self.native_command = native_command
        self.flatpak_command = flatpak_command
        self.tweak_command = tweak_command
        self.native_packages = native_packages
        self.flatpak_packages = flatpak_packages
        self.tweaks = tweaks
        self.service = service
        self.connect("activate", self.on_activate)

    def on_activate(self, app):
        window = MainWindow(self.native_command, self.flatpak_command, self.tweak_command, self.native_packages, self.flatpak_packages, self.tweaks, self.service, application=app)
        window.present()