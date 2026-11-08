SYSTEM_TWEAKS = {
    "DNF Tweaks": {
        "Increase Parallel Downloads": "dnf config-manager setopt max_parallel_downloads=10",
        "Use Fastest Mirrors": "dnf config-manager setopt fastestmirror=True"
    },
    "SELinux": {
        "Disable SELinux": "sed -i 's/SELINUX=enforcing/SELINUX=disabled/' /etc/selinux/config"
    },
    "Services": {
        "Disable Avahi Daemon": "systemctl disable --now avahi-daemon",
        "Disable Bluetooth": "systemctl disable --now bluetooth",
        "Disable Modem Manager (Cellular Modem)": "systemctl disable --now ModemManager",
        "Disable Printer Service": "systemctl disable --now cups",
        "Disable SMART Detection": "systemctl disable --now smartd",
        "Don't Wait For Network On Boot": "systemctl disable --now NetworkManager-wait-online"
    },
    "GRUB": {
        "Optimized GRUB Parameters": '''grubby --update-kernel=ALL --args="amdgpu.ppfeaturemask=0xffffffff split_lock_detect=off amd_pstate=active page_alloc.shuffle=1 pci=pcie_bus_perf pcie_aspm.policy=performance usbcore.autosuspend=-1 nowatchdog nmi_watchdog=0 zswap.enabled=0"'''
    }
}