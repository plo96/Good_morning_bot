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
- Кеширование данных о состоянии бота с помощью redis;
- Дополнительно:
  - Собраны и настроены *docker-* и *docker-compose-* файлы для запуска приложения.

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

## Примечания:
1) Хотя в качестве зависимостей для aiogram тянется pydantic, было решено использовать в качестве схем для ДТО датаклассы (в качестве тренировки).
2) Для запросов к внешним API используется aiohttp, т.к. данная библиотека так же тянется вместе с aiogram. 
3) В качестве llm-нейросети с открытым и понятным api выбрана YandexGPT. 
К сожалению, как и любая услуга в YandexCloud, она является платной с весьма непонятным тарифом и мониторингом для маленьких 
приложений (по крайней мере так показалось создателю данного бота). 
В связи с данным фактом, был введён жесткий лимит по числу пользователей данного бота (изменяется при настройке приложения).
