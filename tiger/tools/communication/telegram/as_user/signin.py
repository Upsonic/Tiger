import asyncio
import time

from telethon.sync import TelegramClient


def signin():
    """ """
    import nest_asyncio

    nest_asyncio.apply()

    async def send_message():
        async with TelegramClient(
                "upsonic_tiger", 21659296,
                "7d0ebd20538d88ab0629eb926acb08f7") as client:
            message = await client.send_message("me", "upsonic_tiger_test")
            await time.sleep(2)
            await message.delelete

    result = asyncio.run(send_message())
    return result


tool_name = "communication.telegram.as_user.signin"
tool_obj = signin
tool_requirements = ["telethon==1.34.0"]
