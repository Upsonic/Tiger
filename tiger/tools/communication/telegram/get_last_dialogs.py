from telethon.sync import TelegramClient
import time
import asyncio


def get_last_dialogs(limit=100):
    import nest_asyncio
    nest_asyncio.apply()

    async def fetch_recent_chats(limit):
        async with TelegramClient("upsonic_tiger", 21659296, '7d0ebd20538d88ab0629eb926acb08f7') as client:
            recent_chats = await client.get_dialogs(limit=limit)
            chat_names = {}
            for chat in recent_chats:
                number = ""
                type_of_entity = ""
                if chat.is_user:
                    number = chat.entity.phone
                    type_of_entity = "user"
                if chat.is_channel:
                    number = chat.entity.username or chat.entity.id
                    type_of_entity = "channel"
                if chat.is_group:
                    number = chat.entity.id
                    type_of_entity = "group"
                chat_names[chat.id] = {"number": number, "title": chat.name or chat.title,
                                       "type_of_entity": type_of_entity, "unread_count": chat.unread_count}
            return chat_names

    chats = asyncio.run(fetch_recent_chats(limit=limit))
    return chats


tool_name = "communication.telegram.get_last_dialogs"
tool_obj = get_last_dialogs
tool_requirements = ["telethon==1.34.0"]
