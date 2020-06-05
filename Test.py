import asyncio
from nio import AsyncClient, Api
from nio.api import ResizingMethod
import os



async def main():
    client = AsyncClient("https://alice.pdxinfosec.org", "@anant:alice.pdxinfosec.org")
    a = await client.login("anant")
    asyncio.run(client.sync_forever(30000))
    if client.should_upload_keys:
        await client.keys_upload()
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
    # #client.content_repository_config()
    # token = client.access_token
    # c = Api.upload(token, "Morty_Smith.jpg")
    # # print(token)
    # path = os.path.dirname(os.path.abspath(__file__))
    # path = os.path.join(path, "Morty_Smith.jpg")
    # a, n = await client.upload(
    #     lambda *_ : path, "image/jpg", "Morty_Smith.jpg"
    # )
    # print(a.content_uri)
    # # thumbObj = await client.thumbnail("https://alice.pdxinfosec.org",a.content_uri,width=500,height=500, method=ResizingMethod.crop)
    # # tubmb_uri = thumbObj.transport_response.real_url
    # # tubmb_uri = str(tubmb_uri)
    # # print(tubmb_uri)
    # b = await client.room_send(
    #     room_id="!pmoszSetEtIHfZScMY:alice.pdxinfosec.org",
    #     message_type="m.room.message",
    #     content={
    #         "msgtype": "m.image",
    #         "body": "Morty_Smith.jpg",
    #         "url" : a.content_uri
    #     }
    # )
    # print(b)
    await client.close()

asyncio.get_event_loop().run_until_complete(main())

