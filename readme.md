# Wyvern Tool

Wyvern tool is a tool aimed at helping make the process of configuring a fresh Fedora installation quick.
It acts as a tool capable of installing native packages, flatpaks, and applying system tweaks to help get
the best performance out of your system.

> [!CAUTION]
> Wyvern Tool makes use of elevated privileges, and if modified may lead to an unusable system.
> Please ensure that you understand the risks of running commands before using this tool.

# Programs

Programs are divided into two categories: Native and Flatpak. For these packages, the program automatically enables 
both RPM Fusion repositories and the Flathub repo for flatpaks.

# Tweaks

> dnf config-manager setopt max_parallel_downloads=10
Option for the DNF package manager, increasing the max number of parallel downloads to 10. 
This is generally considered the sweet spot for stability, though it can be increased further if your network supports it.

> dnf config-manager setopt fastestmirror=True
Option for the DNF package manager, settings the system to attempt to download packages from the fastest available mirrors.

> sed -i 's/SELINUX=enforcing/SELINUX=disabled/' /etc/selinux/config
Disables SELinux. Most users won't notice a difference, though for some SELinux can get in the way of normal system use.

> systemctl disable --now avahi-daemon
Disables the avahi daemon which is mostly used for network printers. 
Note that disabling this service can affect wireless tools like WiVRn.

> systemctl disable --now bluetooth
Disables the bluetooth service at boot.

> systemctl disable --now ModemManager
Disables a service that manages the cellular modem if your device has one.

> systemctl disable --now cups
Disables the printing service at boot.

> systemctl disable --now smartd
Disables smartd service at boot. smartd handles reading HDD SMART reporting for drive health.

> systemctl disable --now NetworkManager-wait-online
The system is allowed to boot before it has an active network. Users will see minimal change but may speed up boot by a few 
seconds.

> grubby --update-kernel=ALL --args="amdgpu.ppfeaturemask=0xffffffff split_lock_detect=off amd_pstate=active page_alloc.shuffle=1 pci=pcie_bus_perf pcie_aspm.policy=performance usbcore.autosuspend=-1 nowatchdog nmi_watchdog=0 zswap.enabled=0
Updates all grub entries with optimized kernel parameters. Changes include AMD pstate support, unlocking OC settings, disabling 
ZSWAP (Fedora uses faster ZRAM), increasing the PCIe payload size, tweaking PCIe power savings, tweaks to USB sleep, and more.