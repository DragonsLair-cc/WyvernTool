TWEAKS = {
    "DNF": {
        "Max_Downloads": "pkexec dnf config-manager setopt max_parallel_downloads=10",
        "Mirror_Speed": "pkexec dnf config-manager setopt fastestmirror=True"
    },
    "Codecs": {
        "Enable Full FFMPEG": "pkexec dnf swap ffmpeg-free ffmpeg --allowerasing",
        "Enable Multimedia Codecs": '''pkexec dnf install @multimedia --setopt="install_weak_deps=False" --exclude=PackageKit-gstreamer-plugin''',
        "Enable AMD GPU Mesa Drivers": "pkexec dnf install mesa-va-drivers-freeworld",
        "Enable AMD GPU Vulkan Drivers": "pkexec dnf install mesa-vulkan-drivers-freeworld"
    }
}