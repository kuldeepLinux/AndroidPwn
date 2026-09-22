from adb_helper import (
    list_devices, take_screenshot, get_battery,
    get_device_info, install_apk, shell_command,
    pull_file, push_file, list_packages,
    uninstall_app, reboot_device, get_ip, clear_screen
)

# Hacker Colors
G = "\033[92m"   # Green
R = "\033[91m"   # Red
Y = "\033[93m"   # Yellow
C = "\033[96m"   # Cyan
B = "\033[94m"   # Blue
M = "\033[95m"   # Magenta
W = "\033[97m"   # White
RESET = "\033[0m"
BOLD = "\033[1m"

BANNER = f"""{G}
   ___           _             _     ___            
  / _ \ _ __   __| |_ __ _   _| | __/ _ \__      ___ __  
 | | | | '_ \ / _` | '__| | | | |/ / | | \ \ /\ / / '_ \ 
 | |_| | | | | (_| | |  | |_| |   <| |_| |\ V  V /| | | |
  \___/|_| |_|\__,_|_|   \__, |_|\_\\___/  \_/\_/ |_| |_|
                         |___/                           
{RESET}{Y}         [ Hacker-Style ADB Tool v1.0 ]{RESET}
{C}         ---------------------------------{RESET}
"""

def show_menu():
    print(BANNER)
    print(f"{G}[{W}1{G}]{W}  📱  List Devices")
    print(f"{G}[{W}2{G}]{W}  📸  Screenshot")
    print(f"{G}[{W}3{G}]{W}  🔋  Battery Status")
    print(f"{G}[{W}4{G}]{W}  📊  Device Info")
    print(f"{G}[{W}5{G}]{W}  📦  Install APK")
    print(f"{G}[{W}6{G}]{W}  💻  Shell Command")
    print(f"{G}[{W}7{G}]{W}  📂  Pull File")
    print(f"{G}[{W}8{G}]{W}  📤  Push File")
    print(f"{G}[{W}9{G}]{W}  📋  List Packages")
    print(f"{G}[{W}10{G}]{W} 🗑️   Uninstall App")
    print(f"{G}[{W}11{G}]{W} 🌐  Get IP Address")
    print(f"{G}[{W}12{G}]{W} 🔄  Reboot Device")
    print(f"{G}[{W}13{G}]{W} 🧹  Clear Screen")
    print(f"{R}[{W}0{R}]{W}  ❌  Exit")
    print(f"{C}{'=' * 45}{RESET}")

def handle_choice(choice):
    if choice == "1":
        print(f"\n{G}[+]{W} Connected Devices:")
        print(list_devices())
    elif choice == "2":
        name = input(f"{Y}[?]{W} Filename (Enter = pwn_screen.png): ").strip() or "pwn_screen.png"
        print(take_screenshot(name))
        print(f"{G}[+]{W} Saved: {name}")
    elif choice == "3":
        print(f"\n{G}[+]{W} Battery Info:")
        print(get_battery())
    elif choice == "4":
        print(f"\n{G}[+]{W} Device Info:")
        print(get_device_info())
    elif choice == "5":
        path = input(f"{Y}[?]{W} APK path: ").strip()
        print(install_apk(path))
    elif choice == "6":
        cmd = input(f"{Y}[?]{W} Shell command: ").strip()
        print(shell_command(cmd))
    elif choice == "7":
        remote = input(f"{Y}[?]{W} Device path: ").strip()
        print(pull_file(remote))
    elif choice == "8":
        local = input(f"{Y}[?]{W} PC path: ").strip()
        remote = input(f"{Y}[?]{W} Device path: ").strip()
        print(push_file(local, remote))
    elif choice == "9":
        print(f"\n{G}[+]{W} Installed Packages:")
        print(list_packages())
    elif choice == "10":
        pkg = input(f"{Y}[?]{W} Package name: ").strip()
        print(uninstall_app(pkg))
    elif choice == "11":
        print(f"\n{G}[+]{W} IP Address:")
        print(get_ip())
    elif choice == "12":
        confirm = input(f"{R}[!]{W} Reboot? (y/n): ").strip().lower()
        if confirm == "y":
            print(reboot_device())
            print(f"{G}[+]{W} Rebooting...")
    elif choice == "13":
        clear_screen()
    else:
        print(f"{R}[!]{W} Invalid choice!")
