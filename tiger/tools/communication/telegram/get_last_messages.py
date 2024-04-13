from telethon.sync import TelegramClient
import time
import asyncio


def get_last_messages(number: str, limit=100):
    import nest_asyncio

    nest_asyncio.apply()

    async def get_messages(num, limit):
        async with TelegramClient(
            "upsonic_tiger", 21659296, "7d0ebd20538d88ab0629eb926acb08f7"
        ) as client:
            messages = await client.get_messages(num, limit=limit)
            the_messages_list = {}
            for each_ms in messages:
                the_messages_list[each_ms.id] = {
                    "id": each_ms.id,
                    "message": each_ms.text,
                    "date": each_ms.date,
                    "sender": (
                        await client.get_entity(each_ms.peer_id.user_id)
                    ).username,
                }
            return the_messages_list

    messages = asyncio.run(get_messages(number, limit))
    return messages


tool_name = "communication.telegram.get_last_messages"
tool_obj = get_last_messages
tool_requirements = ["telethon==1.34.0"]
