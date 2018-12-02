![The Magic Ball-8 Logo](content/ball8_logotext_en.png?raw=true)

Telegram bot ([@ball8en_bot](https://t.me/ball8en_bot)) for emulation of The Magic 8-Ball, a toy used for fortune-telling or seeking advice. [Wiki.](https://en.wikipedia.org/wiki/Magic_8-Ball)

## How to run the bot
1. Download [zip-archive]() or execute the command
    ```sh
    git clone git@github.com:agladky/ball8bot.git
    ```
2. Create a virtual environment
    ```sh
    python3 -m venv ./venv
    ```
3. Install the dependencies
    ```sh
    pip install -r requirements.txt
    ```
4. Rename `config.example.py` into `config.py`
5. Get token at [@BotFather](https://t.me/BotFather) and fill the `bot_token` config parameter
6. Get `/setinline` rights at @BotFather
7. Run a bot
    ```sh
    python main.py
    ```