import asyncio
import time

from telethon.sync import TelegramClient


def get_last_messages(number: str, limit=100):
    """

    :param number: str:
    :param limit:  (Default value = 100)

    """
    import nest_asyncio

    nest_asyncio.apply()

    async def get_messages(num, limit):
        async with TelegramClient(
                "upsonic_tiger", 21659296,
                "7d0ebd20538d88ab0629eb926acb08f7") as client:
            messages = await client.get_messages(num, limit=limit)
            the_messages_list = {}
            for each_ms in messages:
                number = ""
                type_of_entity = ""
                try:
                    number = (await client.get_entity(each_ms.peer_id)).phone
                    type_of_entity = "user"
                except:
                    try:
                        number = (await client.get_entity(each_ms.peer_id)).username
                        type_of_entity = "channel"
                    except:
                        number = (await client.get_entity(each_ms.peer_id)).id
                        type_of_entity = "group"

                the_messages_list[each_ms.id] = {
                    "id":
                    each_ms.id,
                    "message":
                    each_ms.text,
                    "date":
                    each_ms.date,
                    "number":
                    number,
                    "type_of_entity":
                    type_of_entity,
                }
            return the_messages_list

    messages = asyncio.run(get_messages(number, limit))
    return messages


tool_name = "communication.telegram.as_user.get_last_messages"
tool_obj = get_last_messages
tool_requirements = ["telethon==1.34.0"]
