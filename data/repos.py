NATIVE_REPOS = {
    "rpmfusion-free": "https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm",
    "rpmfusion-nonfree": "https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm"
}

FLATPAK_REPOS = {
    "flathub": "https://dl.flathub.org/repo/flathub.flatpakrepo"
}