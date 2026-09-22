#!/usr/bin/env python3
import sys
import shutil
import os
from menu import show_menu, handle_choice, BANNER, G, R, Y, W, RESET

def boot_animation():
    os.system("clear" if os.name != "nt" else "cls")
    print(BANNER)
    print(f"{G}[+]{W} Initializing AndroidPwn...")
    print(f"{G}[+]{W} Loading modules...")
    print(f"{G}[+]{W} Checking ADB...")

def check_adb():
    if shutil.which("adb") is None:
        print(f"{R}[!]{W} ADB not found!")
        print(f"{Y}[i]{W} Install: sudo apt install android-tools-adb")
        sys.exit(1)

def main():
    boot_animation()
    check_adb()
    print(f"{G}[+]{W} System Ready!")
    input(f"{Y}[?]{W} Press ENTER to continue...")

    while True:
        os.system("clear" if os.name != "nt" else "cls")
        show_menu()
        choice = input(f"\n{G}pwn{R}@{G}android{R}:{W}~# ").strip()

        if choice == "0":
            print(f"\n{R}[!]{W} Exiting AndroidPwn...")
            print(f"{G}[+]{W} Goodbye, hacker. 👋")
            break

        try:
            handle_choice(choice)
        except KeyboardInterrupt:
            print(f"\n{R}[!]{W} Interrupted")
        except Exception as e:
            print(f"{R}[!]{W} Error: {e}")

        input(f"\n{Y}[?]{W} Press ENTER to continue...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{R}[!]{W} Exiting...")
        sys.exit(0)
