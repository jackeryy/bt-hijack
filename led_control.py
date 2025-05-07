import asyncio
from bleak import BleakClient

ADDRESS = "BE:67:00:32:E9:69"

async def main():
    async with BleakClient(ADDRESS) as client:
        services = await client.get_services()
        for service in services:
            print(f"Service: {service.uuid}")
            for char in service.characteristics:
                print(f"  Characteristic: {char.uuid} - {char.properties}")

asyncio.run(main())