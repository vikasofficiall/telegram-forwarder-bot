from telethon import TelegramClient, events

api_id = 23550988
api_hash = '687eab2f45e5acf1315ae2cc5e49dbd3'

client = TelegramClient('vikas_auto_bot', api_id, api_hash)

source_channel = 'extrape'
destination_bot = 'extrapebot'

@client.on(events.NewMessage(chats=source_channel))
async def forward_event(event):
    try:
        await client.forward_messages(destination_bot, event.message)
        print("Forwarded full message with media (if any).")
    except Exception as e:
        print(f"Error: {e}")

client.start()
print("Bot is fully running with media forwarding...")

client.run_until_disconnected()
