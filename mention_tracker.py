import logging
import os
import re
import asyncio
from datetime import datetime
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
import aiohttp

load_dotenv('credentials.env')

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Replace these with your actual values
BOT_TOKEN = os.getenv('BOT_TOKEN')
YOUR_USERNAME = os.getenv('YOUR_USERNAME')  # Without the @ symbol
YOUR_CHANNEL_ID = os.getenv('YOUR_CHANNEL_ID')  # Can be username or channel ID

if not all([BOT_TOKEN, YOUR_USERNAME, YOUR_CHANNEL_ID]):
    raise ValueError("Missing one or more required environment variables")

async def start(update: Update, context):
    """Send a message when the command /start is issued."""
    await update.message.reply_text('Bot is running and ready to forward mentions!')

async def generate_message_link(update: Update):
    """Generate a message link with fallback methods"""
    try:
        # Try to get chat username first
        chat_username = update.message.chat.username
        if chat_username:
            return f"https://t.me/{chat_username}/{update.message.message_id}"
        
        # If no username, try to get chat ID and message ID
        chat_id = update.message.chat.id
        message_id = update.message.message_id
        return f"https://t.me/c/{str(chat_id).replace('-100', '')}/{message_id}"
    
    except Exception as e:
        logger.error(f"Error generating message link: {e}")
        return "Message link could not be generated"

def is_mentioned(message_text, username):
    """
    Check if the username is mentioned in the message
    Supports various mention formats:
    - @username
    - @Username
    - @USERNAME
    - Case-insensitive matching
    """
    # Create case-insensitive regex patterns
    mention_patterns = [
        rf'@{re.escape(username)}(?!\w)',  # @username
        rf'@{re.escape(username.lower())}(?!\w)',  # @username
        rf'@{re.escape(username.upper())}(?!\w)',  # @USERNAME
    ]
    
    # Convert message to lowercase for case-insensitive matching
    message_lower = message_text.lower()
    
    # Check if any pattern matches
    for pattern in mention_patterns:
        if re.search(pattern, message_lower):
            return True
    
    return False

async def handle_messages(update: Update, context):
    """Handle incoming messages and check for mentions"""
    # Check if the message contains your username
    if update.message and update.message.text and is_mentioned(update.message.text, YOUR_USERNAME):
        try:
            # Generate message link
            message_link = await generate_message_link(update)
            
            # Forward the original message
            forwarded_message = await context.bot.forward_message(
                chat_id=YOUR_CHANNEL_ID, 
                from_chat_id=update.message.chat_id, 
                message_id=update.message.message_id
            )
            
            # Send a separate message with the link
            await context.bot.send_message(
                chat_id=YOUR_CHANNEL_ID, 
                text=f"Message link: {message_link}",
                reply_to_message_id=forwarded_message.message_id
            )
            
            logger.info(f"Forwarded mention from {update.message.chat.title}")
        except Exception as e:
            logger.error(f"Error forwarding message: {e}")

async def heartbeat():
    """
    Periodic heartbeat function that keeps the application alive
    by sending requests to itself every 5 minutes
    """
    while True:
        try:
            # Get the Render service URL from environment variable
            render_url = os.getenv('RENDER_EXTERNAL_URL')
            
            if render_url:
                async with aiohttp.ClientSession() as session:
                    async with session.get(render_url) as response:
                        logger.info(f"Heartbeat sent at {datetime.now()}, status: {response.status}")
            else:
                logger.info(f"Heartbeat tick at {datetime.now()}")
                
        except Exception as e:
            logger.error(f"Error in heartbeat: {e}")
        
        # Wait for 5 minutes before next heartbeat
        await asyncio.sleep(300)  # 300 seconds = 5 minutes

async def run_bot():
    """Run the bot and heartbeat together"""
    # Create the Application and pass it your bot's token
    application = Application.builder().token(BOT_TOKEN).build()

    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND, 
        handle_messages
    ))

    # Start both the bot and heartbeat
    async with application:
        # Start the heartbeat task
        asyncio.create_task(heartbeat())
        # Start polling
        await application.run_polling(drop_pending_updates=True)

def main():
    """Start the bot."""
    # Run the bot and heartbeat in the event loop
    asyncio.run(run_bot())

if __name__ == '__main__':
    main()