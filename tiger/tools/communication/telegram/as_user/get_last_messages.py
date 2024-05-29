
def get_last_messages(id: int, limit=100):
    """

    :param id: int:
    :param limit:  (Default value = 100)

    """
    import asyncio
    import time

    from telethon.sync import TelegramClient


    id = int(id)
    import nest_asyncio

    nest_asyncio.apply()

    async def get_messages(num, limit):
        async with TelegramClient(
                "upsonic_tiger", 21659296,
                "7d0ebd20538d88ab0629eb926acb08f7") as client:
            messages = await client.get_messages(num, limit=limit)
            the_messages_list = {}
            our_entity_id = (await client.get_me()).id
            for each_ms in messages:
                number = ""
                type_of_entity = ""
                the_entity = await client.get_entity(each_ms.peer_id)
                try:
                    number = the_entity.phone
                    type_of_entity = "user"
                except:
                    try:
                        number = the_entity.username
                        type_of_entity = "channel"
                    except:
                        number = the_entity.id
                        type_of_entity = "group"
                is_me = False
                if our_entity_id == the_entity.id:
                    is_me = True
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
                    "is_me":
                    is_me,
                }
            return the_messages_list

    messages = asyncio.run(get_messages(id, limit))
    return messages


tool_name = "communication.telegram.as_user.get_last_messages"
tool_obj = get_last_messages
tool_requirements = ["telethon==1.34.0"]
