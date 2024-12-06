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
1. Push your code to GitHub
2. Connect your repository to Render
3. Set environment variables in Render dashboard
4. Choose Python runtime
5. Deploy

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