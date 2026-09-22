import subprocess
import os

def run_adb(command, timeout=30):
    try:
        result = subprocess.run(
            f"adb {command}",
            shell=True,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        output = result.stdout.strip()
        error = result.stderr.strip()
        if output:
            return output
        elif error:
            return f"[!] {error}"
        return "[+] Executed"
    except subprocess.TimeoutExpired:
        return "[!] Timeout"
    except Exception as e:
        return f"[!] {e}"

def list_devices():
    return run_adb("devices -l")

def take_screenshot(filename="pwn_screen.png"):
    return run_adb(f"exec-out screencap -p > {filename}")

def get_battery():
    return run_adb("shell dumpsys battery")

def get_device_info():
    model = run_adb("shell getprop ro.product.model")
    android = run_adb("shell getprop ro.build.version.release")
    brand = run_adb("shell getprop ro.product.brand")
    return f"Brand  : {brand}\nModel  : {model}\nAndroid: {android}"

def install_apk(path):
    return run_adb(f"install {path}")

def shell_command(cmd):
    return run_adb(f"shell {cmd}")

def pull_file(remote, local="."):
    return run_adb(f"pull {remote} {local}")

def push_file(local, remote):
    return run_adb(f"push {local} {remote}")

def list_packages():
    return run_adb("shell pm list packages")

def uninstall_app(package):
    return run_adb(f"uninstall {package}")

def reboot_device():
    return run_adb("reboot")

def get_ip():
    return run_adb("shell ip addr show wlan0")

def clear_screen():
    os.system("clear" if os.name != "nt" else "cls")
