import asyncio
from bleak import BleakClient

ADDRESS = "BE:67:00:32:E9:69"  # Replace with your LED's MAC
CHAR_UUID = "0000fff3-0000-1000-8000-00805f9b34fb"  # Target characteristic

# This turns the light RED: 56 R G B 00 F0 AA
RED_COMMAND = bytearray([0x56, 0xFF, 0x00, 0x00, 0x00, 0xF0, 0xAA])
ON_COMMAND = bytearray([0xCC, 0x23, 0x33])
OFF_COMMAND = bytearray([0xCC, 0x24, 0x33])

async def main():
    async with BleakClient(ADDRESS) as client:
        print("Connected:", await client.is_connected())
        await client.write_gatt_char(CHAR_UUID, ON_COMMAND)  # or RED_COMMAND
        print("Command sent")

asyncio.run(main())
