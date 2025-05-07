import pexpect
import time
import re

def strip_ansi(text):
    return re.sub(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])', '', text)

def scan_bluetooth_devices(timeout=20):
    print("---    Scanning for nearby Bluetooth devices    ---")

    scan = pexpect.spawn("bluetoothctl", encoding='utf-8', timeout=timeout)
    scan.logfile = open("pexpect_debug.log","w")
    scan.expect("#")
    scan.sendline("power on")
    scan.expect("#")
    scan.sendline("agent on")
    scan.expect("#")
    scan.sendline("scan on")

    found = {}
    start = time.time()

    try:
        while time.time() - start < timeout:
            line = scan.readline().strip()
            line = strip_ansi(line)
            match = re.search(r"Device ([\w:]+) (.+)", line)
            if match:
                mac, name = match.groups()
                if mac not in found:
                    found[mac] = name
                    print(f"FOUND - {mac} - {name}")
    except pexpect.exceptions.TIMEOUT:
        pass
    finally:
        scan.expect("#")
        scan.sendline("scan off")
        scan.close()

    return found


def choose_device(devices):
    print("\n ----  Select a target device to attack  ----")
    for i, (mac, name) in enumerate(devices.items()):
        print(f"{i+1}. {mac} - {name}")
    choice = int(input("Enter number: ")) - 1
    return list(devices.keys())[choice]

if __name__ == "__main__":
    devices = scan_bluetooth_devices(timeout=12)
    if not devices:
        print("No devices found.")
    else:
        target_mac = choose_device(devices)
        print(f"\nSelected target: {target_mac}")