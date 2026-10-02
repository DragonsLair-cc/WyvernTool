from commands.install import InstallCommand
from commands.tweak import TweakCommand
from services.apply import ApplyService

native_installs = InstallCommand("sudo dnf install -y")
flatpak_installs = InstallCommand("sudo flatpak install -y")
system_tweaks = TweakCommand()

native_installs.toggle("steam", ["steam"], True)
native_installs.run()
native_installs.toggle("steam", ["steam"], False)

system_tweaks.toggle("echo", "echo command 1", True)
system_tweaks.toggle("echo2", "echo command 2", True)

service = ApplyService([native_installs, flatpak_installs, system_tweaks])

service.run_commands()