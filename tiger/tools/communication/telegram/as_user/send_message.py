
def send_message(id: int, message: str) -> str:
    """

    :param id: int:
    :param message: str:

    """
    import asyncio
    import time

    from telethon.sync import TelegramClient


    id = int(id)
    import nest_asyncio

    nest_asyncio.apply()

    async def send_message(number, message):
        async with TelegramClient(
                "upsonic_tiger", 21659296,
                "7d0ebd20538d88ab0629eb926acb08f7") as client:
            return (await client.send_message(number, message)).id

    result = asyncio.run(send_message(id, message))
    return result


tool_name = "communication.telegram.as_user.send_message"
tool_obj = send_message
tool_requirements = ["telethon==1.34.0"]
