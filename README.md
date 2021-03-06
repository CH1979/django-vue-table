# Тестовое задание на вакансию web-программист (Python) в компанию WelbeX
## Задание
>Нужно разработать таблицу в формате Single Page Application.
>
## Требования к таблице.
>1. Таблица должна содержать 4 колонки:
>    1. Дата
>    2. Название
>    3. Количество
>    4. Расстояние
>2. База данных может быть mySQL/PostgreSQL
>3. Таблица должна иметь сортировку по всем полям кроме >даты. Фильтрация должна быть в виде двух выпадающих >списков и текстового поля:
>    1. Выбор колонки, по которой будет фильтрация
>    2. Выбор условия (равно, содержит, больше, меньше)
>    3. Поле для ввода значения для фильтрации
>4. Таблица должна содержать пагинацию
>
>Вся таблица должна работать без перезагрузки страницы.
## Реализация
Для бекэнда использованы Django и Django-Rest-Framework, для фронтэнда - VueJS и Axios, база данных - PostgreSQL. Из-за простоты приложения было принято решение отказаться от использования vue-cli, однофайловых компонент и систем сборки. SPA-приложение реализовано путем подключения скриптов в шаблоне django.
## Запуск приложения
* Для запуска приложения необходимо в файле `.env.dev.example` заполнить пропущенные параметры и сохранить его под именем `.env.dev`
* Запуск приложения производится командой:
```shell
docker-compose up -d --build
```
* Контейнеры с приложением и БД будут собраны и запущены в фоновом (daemon) режиме. База будет наполнена подготовленными данными для демонстрации работы приложения. Приложение будет доступно по адресу: [http://localhost:8000/](http://localhost:8000/)
* Остановка и удаление контейнеров производится командой:
```shell
docker-compose down -v
```
