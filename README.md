# Telegram bot template

This is a template for creating Telegram bots on Python 3.7+ using
[aiogram 3 beta](https://github.com/aiogram/aiogram).  
With Github Actions and Docker.


## How to use
1. Clone this repository
2. Create a new bot(s) using [@BotFather](https://t.me/BotFather) (could be 2 bots for users and for administrators)
3. Create test bot(s) (if you want to test your bot before deploying it)
4. Create 2 files in the root of the project: `.env.production` and `.env.dev`
5. Fill `.env.production` and `.env.dev` files with your bot(s) token(s) and other settings
    - USER_BOT_TOKEN - token of the bot for users
    - ADMIN_BOT_TOKEN - token of the bot for administrators
    - ADMINISTRATOR_IDS - list of administrator IDs (separated by comma)


## Commands
**Run testing bot**
```bash
docker-compose -f docker-compose.yml --env-file=.env.dev up --build
```
