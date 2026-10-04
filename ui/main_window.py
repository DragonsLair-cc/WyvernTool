from gi.repository import Adw, Gtk
from ui.views.install_view import InstallView
from ui.views.tweak_view import TweakView


def placeholder_menu(title, icon):
    return Adw.StatusPage(title=title, description="This menu has not yet been implemented", icon_name=icon)

class MainWindow(Adw.ApplicationWindow):
    def __init__(self, install_native, install_flatpak, tweak_command, native_programs, flatpak_programs, tweak_list, service,  **kwargs):
        super().__init__(**kwargs)
        self.set_title("WyvernTool")
        self.set_default_size(800, 600)
        self.install_native = install_native
        self.install_flatpak = install_flatpak
        self.tweak_command = tweak_command
        self.service = service
        self.native_programs = native_programs
        self.flatpak_programs = flatpak_programs
        self.tweak_list = tweak_list

        tabs = [
            ("install", "Install", "system-software-install-symbolic"),
            ("tweaks", "Tweaks", "applications-system-symbolic"),
            # Not sure if I want to make a customization tab yet
            #("customize", "Customize", "preferences-desktop-appearance-symbolic")
        ]

        views = {
            "install": InstallView(self.install_native, self.install_flatpak, self.native_programs, self.flatpak_programs),
            "tweaks": TweakView(self.tweak_command, self.tweak_list)
        }

        stack = Adw.ViewStack()
        for view_id, title, icon in tabs:
            if view_id in views:
                view = views[view_id]
            else:
                view = placeholder_menu(title, icon)
            stack.add_titled_with_icon(view, view_id, title, icon)

        switcher = Adw.ViewSwitcher()
        switcher.set_stack(stack)
        switcher.set_policy(Adw.ViewSwitcherPolicy.WIDE)

        install_button = Gtk.Button(label="Install")
        install_button.add_css_class("suggested-action")
        install_button.connect("clicked", self.on_apply_clicked)

        header = Adw.HeaderBar()
        header.set_title_widget(switcher)
        header.pack_end(install_button)
        #content = Gtk.Label(label="Window Content")

        layout = Adw.ToolbarView()
        layout.add_top_bar(header)
        layout.set_content(stack)

        self.set_content(layout)

    def on_apply_clicked(self, _button):
        self.service.run_commands()