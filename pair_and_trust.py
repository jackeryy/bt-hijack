import pexpect

def pair_and_trust(mac):
    print(f"---   Pairing and trusting {mac}   ---")
    bt = pexpect.spawn("bluetoothctl", encoding='utf-8', timeout=10)

    bt.expect("#")
    bt.sendline("power on")
    bt.expect("#")
    bt.sendline("agent on")
    bt.expect("#")
    bt.sendline("default-agent")
    bt.expect("#")
    bt.sendline("scan on")
    bt.expect("#")
    bt.sendline(f"pair {mac}")
    bt.expect("#")
    bt.sendline("trust {mac}")
    bt.expect("#")
    bt.sendline(f"connect {mac}")
    bt.expect("#", timeout=5)
    bt.sendline(f"disconnect {mac}")
    bt.expect("#", timeout=5)
    bt.sendline("exit")
    bt.close()

    print(f"\n---   Pairing and trusting {mac} complete.   ---")
    
if __name__ == "__main__":
    mac = input("Enter the MAC address of the target device: ")
    pair_and_trust(mac)