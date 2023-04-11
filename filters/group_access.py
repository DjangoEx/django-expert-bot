from pyrogram import Client
from pyrogram.types import Message
from pyrogram.enums import ChatMemberStatus


async def is_owner(client: Client, m: Message):
    chat_member = await client.get_chat_member(m.chat.id, m.from_user.id)
    return chat_member.status == ChatMemberStatus.OWNER


async def is_administrator(client: Client, m: Message):
    chat_member = await client.get_chat_member(m.chat.id, m.from_user.id)
    return chat_member.status in (
        ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR
    )
