import sys

from services.startup import StartupService
from services.apply import ApplyService
from commands.install import InstallCommand
from commands.tweak import TweakCommand
from data.repos import NATIVE_REPOS
from data.repos import FLATPAK_REPOS
from data.programs import NATIVE_PROGRAMS
from data.programs import FLATPAK_PROGRAMS
from data.tweaks import SYSTEM_TWEAKS
from ui.app import WyvernTool

start_service = StartupService(NATIVE_REPOS, FLATPAK_REPOS)
start_service.repo_check()

native_install_command = InstallCommand("dnf install")
flatpak_install_command = InstallCommand("flatpak install")
tweak_command = TweakCommand()

apply_service = ApplyService([native_install_command, flatpak_install_command, tweak_command])

app = WyvernTool(native_install_command, flatpak_install_command, tweak_command, NATIVE_PROGRAMS, FLATPAK_PROGRAMS, SYSTEM_TWEAKS, apply_service)
sys.exit(app.run(sys.argv))