Remaining time
==========

Remaining time создан и модифицируется в течение обучения.


Цель проекта
------------

Создать телеграм-бота, который бы считал, сколько вам осталось жить в часах. Ведь порой мы не ценим время, которое тратим на нашу жизнь. 

Настройка
---------

Создайте файл settings.py и добавьте туда следующие настройки:

.. code-block:: python

    PROXY = {'proxy_url': 'socks5://ВАШ_SOCKS5_ПРОКСИ:1080',
            'urllib3_proxy_kwargs': {'username': 'ЛОГИН', 'password': 'ПАРОЛЬ'}}

    API_KEY = 'API ключ, который вы получили у BotFather'
    

Необходимо установить библиотеки telegram-bot, logging

Запуск
------

В активированном виртуальном окружении выполните:

.. code-block:: text

    python3 bot.py
    


Отправьте сообщение боту:

.. code-block:: text

    /life number  - где number это то, сколько вам лет сейчас.


.. _Learn Python: https://learn.python.ru/
