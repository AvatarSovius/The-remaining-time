The remaining time
==========

The remaining time создан и модифицируется в течение обучения основам языка Python и изучения ботостроения.


Цель проекта
------------

Создать Telegram бота, который будет напоминать вам о ценности времени и о том, как оно скоротечно. Задумайся, ведь жить вам осталось не так много, бот будет напоминать вам, сколько вам осталось жить в часах.

Настройка
---------

Создайте файл settings.py и добавьте туда следующие настройки:

.. code-block:: python

    PROXY = {'proxy_url': 'socks5://ВАШ_SOCKS5_ПРОКСИ:1080',
            'urllib3_proxy_kwargs': {'username': 'ЛОГИН', 'password': 'ПАРОЛЬ'}}

    TELEGRAM_TOKEN = 'API ключ, который вы получили у BotFather'


Необходимо установить библиотеки telegram-bot

Запуск
------

В активированном виртуальном окружении выполните:

.. code-block:: text

    python3 bot.py



Отправьте сообщение боту:

.. code-block:: text

    /life number - где number, это число ваших лет


.. _Learn Python: https://learn.python.ru/
