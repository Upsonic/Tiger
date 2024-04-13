from telethon.sync import TelegramClient
import time
import asyncio


def delete_message(number: str, message: str):
    import nest_asyncio

    nest_asyncio.apply()

    async def del_message(num, message):
        async with TelegramClient(
            "upsonic_tiger", 21659296, "7d0ebd20538d88ab0629eb926acb08f7"
        ) as client:
            await client.delete_messages(num, message)

    asyncio.run(del_message(number, message))


tool_name = "communication.telegram.delete_message"
tool_obj = delete_message
tool_requirements = ["telethon==1.34.0"]
