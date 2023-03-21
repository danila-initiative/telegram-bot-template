# Telegram bot template

This is a template for Python project. Particularly, for Telegram bots on
[aiogram 3 beta](https://github.com/aiogram/aiogram).  
With CI/CD using GitHub Actions, Docker and GitHub Packages. All secrets are stored in GitHub Secrets.  
Described some repository settings for collaboration with other developers.


## How to use
1. Clone this repository
2. Create a new bot(s) using [@BotFather](https://t.me/BotFather)
3. Create test bot(s) (if you want to test your bot before deploying it)
4. Create .env file for local development
5. Fill `.env` file with your bot(s) token(s) and other settings if necessary
    - USER_BOT_TOKEN - token of the bot for users
6. To run your bot in container use `Run testing bot` command (see below)

<br>

## To deploy your bot(s) to the server
1. Create a new server with installed Docker
2. Create new GitHub Access token
   - Go to https://github.com/settings/tokens
   - Press `Generate new token` (classic)
   - Select scopes: `write:packages`, `read:packages`, `delete:packages`
   - Copy your token or do not close the page, you will need it later
3. Create secrets in your repository settings (Settings -> Secrets and Variables -> Actions):
   - PRODUCTION_SSH_HOST - IP address of your server
   - PRODUCTION_SSH_USERNAME - username for SSH connection to your server
   - PRODUCTION_SSH_KEY - private key for SSH connection to your server
   - USER_BOT_TOKEN - token of the user production bot
   - TOKEN - GitHub token (see step 2)
4. Change PROJECT_NAME envirinment in `deploy.yml`
5. Add tag to your repository and deployment will start automatically (could check in Actions tab)

<br>

## Commands
### Format code
```bash
make format
```

### Check code style and analyze code
```bash
make check-pep8
```

### Run testing bot
```bash
docker-compose -f docker-compose.dev.yml up --build
```

### Enter into the container
```bash
docker exec -it <container_name> bash
docker exec -it telegram_bot_template bash
```

### Check bot process
```bash
supervisorctl status
```

### Restart bot process
```bash
supervisorctl restart user-bot
```

<br>

## Full project tree
```bash
├── .github
│   └── workflows
│       ├── check-pep8.yml
│       └── deploy.yml
├── code
│   ├── __init__.py
│   ├── docs
│   ├── handlers
│   │   └── __init__.py
│   ├── internal
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── db.py
│   ├── keyboards
│   │   └── __init__.py
│   ├── scripts
│   │   └── migrate.py
│   ├── storage
│   │   ├── migrations
│   │   │   └── 001_CREATE_USER_TABLE.sql
│   │   └── queries
│   │       └── add_new_user.sql
│   └── user_bot.py
├── data
│   ├── python_user.stderr.log
│   ├── python_user.stdout.log
│   └── sqlite.db
├── .dockerignore
├── .gitignore
├── Dockerfile
├── docker-compose.dev.yml
├── docker-compose.production.yml
├── Makefile
├── pyproject.toml
├── README.md
├── requirements.txt
├── setup.cfg
└── supervisor.conf
```