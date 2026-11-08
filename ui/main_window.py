from gi.repository import Adw, Gtk
from ui.views.native_install_view import NativeInstallView
from ui.views.flatpak_install_view import FlatpakInstallView
from ui.views.system_tweaks_view import SystemTweaksView

def placeholder_menu(title, icon):
    return Adw.StatusPage(title=title, description="Not Implemented", icon_name=icon)

class MainWindow(Adw.ApplicationWindow):
    def __init__(self, native_command, flatpak_command, tweak_command, native_packages:dict, flatpak_packages:dict, tweaks:dict, service, **kwargs):
        super().__init__(**kwargs)
        self.set_title("Wyvern Tool")
        self.set_default_size(800,800)
        self.service = service

        tabs = [
            ("native_install", "Install", "system-software-install-symbolic"),
            ("flatpak_install", "Flatpaks", "system-software-install-symbolic"),
            ("tweaks", "Tweaks", "applications-system-symbolic")
        ]

        views = {
            "native_install": NativeInstallView(native_command, native_packages),
            "flatpak_install": FlatpakInstallView(flatpak_command, flatpak_packages),
            "tweaks": SystemTweaksView(tweak_command, tweaks),
        }

        stack = Adw.ViewStack()
        for view_id, title, icon in tabs:
            if view_id in views:
                view = views[view_id]
            else:
                view = placeholder_menu(title, icon)
            stack.add_titled_with_icon(view, view_id, title, icon)

        view_switcher = Adw.ViewSwitcher()
        view_switcher.set_stack(stack)
        view_switcher.set_policy(Adw.ViewSwitcherPolicy.WIDE)

        apply_button = Gtk.Button(label="Apply")
        apply_button.add_css_class("suggested-action")
        apply_button.connect("clicked", self.on_apply_clicked)

        header = Adw.HeaderBar()
        header.set_title_widget(view_switcher)
        header.pack_end(apply_button)

        layout = Adw.ToolbarView()
        layout.add_top_bar(header)
        layout.set_content(stack)

        self.set_content(layout)

    def on_apply_clicked(self, _button):
        self.service.run_commands()