import asyncio
import time

from telethon.sync import TelegramClient


def send_message(number: str, message: str) -> str:
    """

    :param number: str:
    :param message: str:

    """
    import nest_asyncio

    nest_asyncio.apply()

    async def send_message(number, message):
        async with TelegramClient(
            "upsonic_tiger", 21659296, "7d0ebd20538d88ab0629eb926acb08f7"
        ) as client:
            return (await client.send_message(number, message)).id

    result = asyncio.run(send_message(number, message))
    return result


tool_name = "communication.telegram.send_message"
tool_obj = send_message
tool_requirements = ["telethon==1.34.0"]
