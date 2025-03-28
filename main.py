import asyncio
from telethon import TelegramClient
from bot.config import Telegram

# Your bot credentials
API_ID = Telegram.API_ID
API_HASH = Telegram.API_HASH
BOT_TOKEN = Telegram.BOT_TOKEN
AUTH_CHANNEL = Telegram.AUTH_CHANNEL  # The force-subscribe channel

# Initialize client
client = TelegramClient("test_session", API_ID, API_HASH).start(bot_token=BOT_TOKEN)

async def test_bot():
    print("✅ Testing bot start command...")

    # Send /start command
    async with client as bot:
        message = await bot.send_message("me", "/start")
        print(f"📩 Sent: {message.text}")

        # Wait for bot response
        async for response in bot.iter_messages("me", limit=1):
            print(f"🤖 Bot Response: {response.text}")
            if "Join our channel" in response.text:
                print("✅ Force Subscription is working!")

                # Simulate user joining channel
                print("📌 Simulating user joining the channel...")
                await asyncio.sleep(2)  # Wait for 2 seconds (simulate delay)

                # Send /start again after joining
                message = await bot.send_message("me", "/start")
                async for response in bot.iter_messages("me", limit=1):
                    print(f"🤖 New Bot Response: {response.text}")
                    if "Welcome" in response.text:
                        print("✅ Bot is working correctly after joining!")
                    else:
                        print("❌ Bot still blocking even after joining!")

# Run the test
asyncio.run(test_bot())