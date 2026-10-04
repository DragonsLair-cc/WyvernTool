from gi.repository import Adw
from ui.main_window import MainWindow

class WyvernTool(Adw.Application):
    def __init__(self, install_native, install_flatpak, tweak_command, native_programs, flatpak_programs, tweak_list, service):
        super().__init__(application_id="io.github.wyvern.WyvernTool")
        self.install_native = install_native
        self.native_programs = native_programs
        self.install_flatpak = install_flatpak
        self.tweak_command = tweak_command
        self.flatpak_programs = flatpak_programs
        self.tweak_list = tweak_list
        self.service = service
        self.connect("activate", self.on_activate)

    def on_activate(self, app):
        window = MainWindow(self.install_native, self.install_flatpak, self.tweak_command, self.native_programs, self.flatpak_programs, self.tweak_list, self.service, application = app)
        window.present()