# Telegram Mention Tracker Bot

## 📌 Project Overview

This Telegram bot automatically forwards messages that mention a specific username to a designated channel. It supports case-insensitive username matching and provides a direct link to the original message.

## ✨ Features

- Case-insensitive username mention detection
- Automatic message forwarding to a specific channel
- Generates message links for easy tracking
- Supports both public and private groups
- Logging for monitoring bot activities

## 🛠 Prerequisites

- Python 3.10+
- Telegram Bot API Token
- Telegram Channel for message forwarding

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Hr-Panahi/Telegram-Mention-Tracker.git
cd Telegram-Mention-Tracker
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `credentials.env` file in the project root:
```
BOT_TOKEN=your_telegram_bot_token
YOUR_USERNAME=your_telegram_username_without_@
YOUR_CHANNEL_ID=your_channel_username_or_id
```

## 🤖 Bot Setup

### 1. Create a Telegram Bot
- Talk to BotFather on Telegram
- Create a new bot with `/newbot`
- Save the bot token

### 2. Add Bot to Groups and Channel
- Add the bot to the group where you want to monitor mentions
- Add the bot as an admin to your target channel
- Ensure the bot has message forwarding permissions

## 🌐 Deployment

### Local Development
```bash
python bot_script.py
```

### Online Deployment
Recommended platforms:
- Render
- Railway
- PythonAnywhere

### Render Deployment Steps
1. Create a GitHub repository for your bot.
2. Push your code to GitHub if you haven’t already.
3. Sign up on Render.com.
4. Create a new Web Service on Render.
5. Connect your GitHub repository to Render.
6. Configure the build and start commands:
  * Build Command: `pip install -r requirements.txt`
  * Start Command: `python mention_tracker.py`
7. Set up environment variables (e.g., BOT_TOKEN, YOUR_USERNAME, YOUR_CHANNEL_ID) in the Render dashboard under your service's settings.
Render will automatically deploy your bot and keep it running, handling the environment setup and any future deployments when you push updates to your GitHub repository.

## 🔧 Customization

Modify `bot_script.py` to:
- Change mention detection logic
- Add more sophisticated forwarding rules
- Implement additional logging

## 🔒 Security Notes

- Never share your bot token publicly
- Use environment variables for sensitive information
- Limit bot permissions to necessary actions

## 📋 Troubleshooting

- Ensure bot has correct permissions
- Check environment variable configuration
- Verify Telegram API token is valid
- Review logs for error messages

## 📝 License

[Choose an appropriate license, e.g., MIT License]

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📞 Support

For issues or questions, please open a GitHub issue in the repository.