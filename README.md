# 🎲 Deathroll Discord Bot

A fun Discord bot built with **Python** that lets users challenge each other to a game of **Deathroll** — a high-stakes dice game where players roll down from 1000 until someone rolls a 1 and loses.  

---

## 📑 Table of Contents
- [Introduction](#-introduction)  
- [Features](#-features)  
- [Installation](#-installation)  
- [Configuration](#-configuration)  
- [Usage](#-usage)  
- [Examples](#-examples)  
- [Dependencies](#-dependencies)  
- [Troubleshooting](#-troubleshooting)  
- [Contributors](#-contributors)  
- [License](#-license)  

---

## 🎮 Introduction
This bot allows users to:  
- Start a **Deathroll** duel with another member.  
- Take turns rolling until someone inevitably rolls a **1**.  
- Forfeit or end the game at any time.  
- Invite the bot to other servers via a dynamic invite link.  

It was created using Python, **discord.py**, and inspiration from YouTube tutorials and AI assistance.

---

## ✨ Features
- 🔥 Start a **Deathroll duel** between two players.  
- 🎲 Fair (but slightly biased) random number rolls.  
- 🏳 Forfeit option for when you want to give up.  
- 🛑 Forcefully end games if needed.  
- 📩 Generate an **invite link** dynamically.  

---

## ⚙️ Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/deathroll-bot.git
   cd deathroll-bot
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:  
   Create a `.env` file in the project root with:
   ```ini
   DISCORD_TOKEN=your-bot-token-here
   DISCORD_CLIENT_ID=your-bot-client-id-here
   ```

4. **Run the bot**:
   ```bash
   python main.py
   ```

---

## 🛠 Configuration
- **DISCORD_TOKEN** → Your bot’s authentication token.  
- **DISCORD_CLIENT_ID** → Your bot’s client/application ID.  
- Permissions are set dynamically when generating an invite link (`!invite`).  

---

## 🚀 Usage
Once the bot is running in your server, use the following commands:

- `!invite` → Get a link to invite the bot to other servers.  
- `!deathroll @opponent` → Start a new Deathroll game with a mentioned user.  
- `!roll <number>` → Roll the dice (must match the current number).  
- `!forfeit` → Forfeit the game and declare the opponent as the winner.  
- `!finish` → End the current game without a winner.  

---

## 📌 Examples
```
User1: !deathroll @User2
Bot: 🔥 Deathroll started between @User1 and @User2!  
     @User1, type `!roll 1000` to start.

User1: !roll 1000
Bot: 🎲 @User1 rolled 823 (1-1000)  
     🔄 @User2, type `!roll 823` to continue!
```

---

## 📦 Dependencies
- [discord.py](https://pypi.org/project/discord.py/)  
- [python-dotenv](https://pypi.org/project/python-dotenv/)  

Install them via:
```bash
pip install discord.py python-dotenv
```

---

## 🐞 Troubleshooting
- **Bot doesn’t respond to commands** → Ensure `MESSAGE CONTENT INTENT` is enabled in the Discord Developer Portal.  
- **Invalid Token error** → Double-check your `.env` file values.  
- **Game won’t start** → Make sure you mention an opponent (`!deathroll @username`).  

---

## 👥 Contributors
- **You** – Project creator  
- **YouTube tutorials & AI tools** – For guidance and inspiration  

---

## 📜 License
This project is open-source. You may use, modify, and distribute it freely.  
