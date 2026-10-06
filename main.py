import sys

from commands.install import InstallCommand
from commands.tweak import TweakCommand
from data.programs import NATIVE_PROGRAMS
from data.programs import FLATPAK_PROGRAMS
from data.tweaks import TWEAKS
from services.apply import ApplyService
from ui.app import WyvernTool

install_native = InstallCommand("dnf install -y")
install_flatpak = InstallCommand("flatpak install -y")
tweak_command = TweakCommand()
service = ApplyService([install_native, install_flatpak, tweak_command])

app = WyvernTool(install_native, install_flatpak, tweak_command, NATIVE_PROGRAMS, FLATPAK_PROGRAMS, TWEAKS, service)
sys.exit(app.run(sys.argv))