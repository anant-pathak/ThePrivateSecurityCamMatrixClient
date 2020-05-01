import asyncio
from nio import AsyncClient

async def main():
    client = AsyncClient("https://alice.pdxinfosec.org", "@anant:alice.pdxinfosec.org")
    a = await client.login("anant")
    print(a)
    b = await client.room_send(
        room_id="!pmoszSetEtIHfZScMY:alice.pdxinfosec.org",
        message_type="m.room.message",
        content={
            "msgtype": "m.text",
            "body": "Hello World"
        }
    )
    print(b)
    await client.close()

asyncio.get_event_loop().run_until_complete(main())

