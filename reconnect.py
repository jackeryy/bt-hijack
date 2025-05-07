import pexpect

def reconnect(mac):
    print(f"Attempting to reconnect to {mac}...")

    bt = pexpect.spawn("bluetoothctl", encoding='utf-8', timeout=10)
    bt.expect("#")
    bt.sendline("power on")
    bt.expect("#")
    bt.sendline("agent on")
    bt.expect("#")
    bt.sendline("default-agent")
    bt.expect("#")
    bt.sendline(f"connect {mac}")
    bt.expect("#", timeout=5)

    bt.sendline("exit")
    bt.close()

    print("Reconnect attempt complete.")


if __name__ == "__main__":
    target_mac = input("Enter the MAC address of the speaker: ")
    reconnect(target_mac)