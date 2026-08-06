"""Example usage of pydelijn (run manually, not a pytest test)."""

import asyncio

from pydelijn import DeLijnClient


async def main() -> None:
    """Search a stop, then print its upcoming passages."""
    api_key = "<put your data.delijn.be subscription key here>"

    async with DeLijnClient(api_key) as client:
        stops = await client.search_stops("Antwerpen Rooseveltplaats")
        if not stops:
            print("No stops found")
            return
        stop = stops[0]
        print(f"Stop: {stop.name} ({stop.number}) - {stop.municipality}")

        passages = await client.get_passages(stop.number, max_passages=10)
        for passage in passages:
            print("----------------------------------------")
            print(f"Line: {passage.line.public_number} - {passage.line.description}")
            print(f"Direction: {passage.direction}")
            print(f"Destination: {passage.destination}")
            print(f"Due at: {passage.due_at}")
            print(f"Realtime: {passage.is_realtime}, Cancelled: {passage.cancelled}")


if __name__ == "__main__":
    asyncio.run(main())
