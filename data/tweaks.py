TWEAKS = {
    "DNF": {
        "Max_Downloads": ["dnf config-manager setopt max_parallel_downloads=10"],
        "Mirror_Speed": ["dnf config-manager setopt fastestmirror=True"]
    },
    "Codecs": {
        "Enable Full FFMPEG": ["dnf swap -y ffmpeg-free ffmpeg --allowerasing", '''dnf install -y @multimedia --setopt="install_weak_deps=False" --exclude=PackageKit-gstreamer-plugin'''],
        "Enable AMD GPU Freeworld Drivers": ["dnf install -y mesa-va-drivers-freeworld", "dnf swap -y mesa-vulkan-drivers{,-freeworld}"],
    }
}