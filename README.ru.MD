![Логотип Магический шар 8](content/ball8_logotext_ru.png?raw=true)

Телеграм бот ([@ball8ru_bot](https://t.me/ball8ru_bot)) для эмуляции Магического шара 8, шуточной игрушки для предсказания будущего. [Побробнее.](https://ru.wikipedia.org/wiki/Magic_8_ball)

## Как запустить
1. Загрузить [zip-архив]() или выполнить команду
    ```sh
    git clone git@github.com:agladky/ball8bot.git
    ```
2. Создать виртуальное окружение
    ```sh
    python3 -m venv ./venv
    ```
3. Установить зависимости
    ```sh
    pip install -r requirements.txt
    ```
4. Переименовать `config.example.py` в `config.py`
5. Получить токен у [@BotFather](https://t.me/BotFather) и записать в переменную `bot_token`
6. Запросить `/setinline` права у @BotFather
7. Запустить бота командой
    ```sh
    python main.py
    ```