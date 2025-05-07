import pexpect
import time
import re

def scan_bluetooth_devices(timeout=10):
    print("[*] Scanning for nearby Bluetooth devices")

    scan = pexpect.spawn("bluetoothctl", encoding='utf-8', timeout=timeout)
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
            match = re.search(r"\[NEW\] Device ([\w:]+) (.+)", line)
            if match:
                mac, name = match.groups()
                found[mac] = name
                print(f"{mac} - {name}")
    except pexpect.exceptions.TIMEOUT:
        pass
    finally:
        scan.sendline("scan off")
        scan.close()

    return found


def choose_device(devices):
    print("\n[*] Select a target device to attack:")
    for i, (mac, name) in enumerate(devices.items()):
        print(f"{i+1}. {mac} - {name}")
    choice = int(input("Enter number: ")) - 1
    return list(devices.keys())[choice]

if __name__ == "__main__":
    devices = scan_bluetooth_devices(timeout=10)
    if not devices:
        print("No devices found.")
    else:
        target_mac = choose_device(devices)
        print(f"\nSelected target: {target_mac}")