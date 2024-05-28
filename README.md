# Telegram Good Morning Bot
## Описание

Телеграмм-бот, отправляющий ежедневные уведомления в утреннее время.
Уведомления включают в себя пожелание доброго утра (сгенерированное нейросетью) и прогноз погоды на текущий день.

Реализованы технологии:
- Асинхронный телеграмм-бот;
- Обращение с данными через dataclasses;
- Нереляционная база данных (Mongodb);
- Асинхронный доступ к БД;
- Асинхронное выполнение задач по расписанию;
- Обращение к внешним API;
- Кеширование данных о состоянии бота с помощью redis;
- Дополнительно:
  - Собраны и настроены *docker-* и *docker-compose-* файлы для быстрого запуска приложения.
  - Создан кастомный логгер с отправкой важных сообщений в телеграм-чат админу.

## Основной используемый стек технологий:

- Python:
  - aiogram
  - APScheduler
  - motor
  - aiohttp
  - dataclasses
- Mongodb
- Redis
- docker, docker-compose

## Запуск и настройка
1) Получить все необходимые ключи внешних API для работы приложения:
   - YOUR_BOT_TOKEN: написать телеграм-боту Bot_Father, выбрать комманду '/create_bot' и следовать инструкциям.
   - YOUR_WEATHER_API_KEY: зарегистрироваться на сайте openweathermap.com и выбрать раздел ...
   - YOUR_GEOPOSITIONAL_API_KEY: в штатной вариации - такой же ключ 'YOUR_WEATHER_API_KEY'.
   - YOUR_YANDEX_IDENTIFICATON: зарегистрироваться на сайте yandex-cloud.ru и выбрать раздел ...
   - YANDEX_GPT_API_KEY: зарегистрироваться на сайте yandex-cloud.com.ru и выбрать раздел ...
2) Создать в корне приложения .env по образцу и внести в него полученные в п.1 ключи (при необходимости изменить кофигурации MongoDB и Redis, добавить телеграм-id администратора и раскомментировать строку с 'ADMIN_ID'):
    ```plaintext
        # MongoDB configs
        MONGO_HOST=localhost  
        MONGO_PORT=27017
        MONGO_USER=admin
        MONGO_PWD=admin
  
        # Redis-server configs
        REDIS_PWD=admin
        REDIS_HOST=localhost
        REDIS_PORT=6379
        
        # Telegram configs
        BOT_TOKEN=YOUR_BOT_TOKEN
        # ADMIN_ID=YOUR_ADMIN_ID        
        MAX_NUMBER_OF_USERS=10
  
        # Outer APIs configs        
        OPENWEATHERMAP_API_KEY=YOUR_WEATHER_API_KEY
        GEOPOSITIONAL_OPENWEATHERMAP_API_KEY=YOUR_GEOPOSITIONAL_API_KEY
        YANDEX_GPT_IDENTIFICATION=YOUR_YANDEX_IDENTIFICATON
        YANDEX_GPT_API_KEY=YOUR_LLM_API_KEY
   
3) Находясь в директории с приложением выполнить в терминале команду:
   > 'docker-compose up --build -d' - для запуска контейнеров с БД и приложением.
   
   > 'docker-compose down' - для остановки всех работающих контейнеров и их удаления.

## Примечания:
1) Хотя в качестве зависимостей для aiogram тянется pydantic, было решено использовать в качестве схем для ДТО датаклассы (в качестве тренировки).
2) Для запросов к внешним API используется aiohttp, т.к. данная библиотека так же тянется вместе с aiogram. 
3) В качестве llm-нейросети с открытым и понятным api выбрана YandexGPT. 
К сожалению, как и любая услуга в YandexCloud, она является платной с весьма непонятным тарифом и мониторингом для маленьких 
приложений (по крайней мере так показалось создателю данного бота). 
В связи с данным фактом, был введён жесткий лимит по числу пользователей данного бота (изменяется при настройке приложения).
