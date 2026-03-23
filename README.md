# Real-time To-Do List API (Lab 02)

**Студентка:** Надія Щербина 
**Група:** КВ-51мн  
**Лабораторна робота: №2:** Організація спільної роботи користувачів Web-додатка  
## Посилання на звіт 
[https://docs.google.com/document/d/16yPPVKSbs7w5lMctBZtDBXpKvrG-EGOqfcSWl_vC1DU/edit?usp=sharing
](https://docs.google.com/document/d/1vVYE2JYzs-A2lpHH9Tr6KwdCgSVvTFX2I6lxFhFcy-o/edit?usp=sharing)
---

## Опис завдання
Цей проєкт є вдосконаленою версією стандартного API списку справ. Він інтегрує **WebSockets** через **Django Channels**, щоб забезпечити миттєву синхронізацію даних між усіма підключеними клієнтами. Коли завдання створюється, оновлюється або видаляється через REST API, усі активні користувачі бачать зміни одразу, без необхідності оновлення сторінки.

## Функції в режимі реального часу
- ✅ **Миттєві оновлення завдань:** синхронізація дій «Створити/Оновити/Видалити» між клієнтами в режимі реального часу.
- ✅ **Відстеження присутності:** список «Користувачі в мережі» для адміністраторів у режимі реального часу.
- ✅ **Інформаційна панель у режимі реального часу:** спеціальна англомовна сторінка для моніторингу активності системи.
- ✅ **Інтеграція з адміністративною панеллю:** Автоматичне відстеження підключень/відключень користувачів у панелі адміністратора Django.
- ✅ **Паралельність:** Використання Redis як посередника повідомлень для високошвидкісної передачі даних.

## Технології
- **Backend:** Python 3.12+, Django 6.0+
- **Real-time:** Django Channels 4.2+, Daphne (ASGI)
- **Database:** SQLite (Relational), Redis 7.0 (Message Broker via Docker)
- **API:** Django REST Framework, Swagger (drf-spectacular)
- **Frontend:** JavaScript (WebSockets), Bootstrap 5

---

## Встановлення та запуск

1. **Клонування репозиторію**
   ```bash
   git clone [https://github.com/nadiina/realtime-todo-api.git](https://github.com/nadiina/realtime-todo-api.git)
   cd realtime-todo-api/django
   ```
Створення віртуального середовища:
 ```Bash
python -m venv venv
 ```
# Windows:
 ```Bash
.\venv\Scripts\activate
 ```
# Linux/Mac:
```Bash
source venv/bin/activate
Install dependencies:
```

```Bash
pip install -r requirements.txt
Start Redis via Docker:
```

```Bash
docker run -d -p 6379:6379 --name my-redis redis:alpine
Apply database migrations:
```
```Bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
Run the development server:
```
```Bash
python manage.py runserver
```
