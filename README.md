# Real-time To-Do List API (Lab 02)

**Student:** Nadiia Щербина 
**Group:** КВ-51мн  
**Project:** Real-time Task Management System  

---

## Project Overview
This project is an evolution of a standard To-Do List API. It integrates **WebSockets** via **Django Channels** to provide instant data synchronization across all connected clients. When a task is created, updated, or deleted via the REST API, all active users see the changes immediately without refreshing the page.

## Real-time Features
- ✅ **Instant Task Updates:** Live synchronization of Create/Update/Delete actions across clients.
- ✅ **Presence Tracking:** Real-time "Users Online" list for administrators.
- ✅ **Live Dashboard:** Dedicated English-language monitoring page for system activity.
- ✅ **Admin Integration:** Automated tracking of user connections/disconnections in the Django Admin panel.
- ✅ **Concurrency:** Powered by Redis as a message broker for high-speed data delivery.

## Tech Stack
- **Backend:** Python 3.12+, Django 6.0+
- **Real-time:** Django Channels 4.2+, Daphne (ASGI)
- **Database:** SQLite (Relational), Redis 7.0 (Message Broker via Docker)
- **API:** Django REST Framework, Swagger (drf-spectacular)
- **Frontend:** JavaScript (WebSockets), Bootstrap 5

---

## Installation & Setup

### Prerequisites
- Python 3.12 or higher
- Docker Desktop (for running Redis)

### Step-by-Step Guide

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/nadiina/realtime-todo-api.git](https://github.com/nadiina/realtime-todo-api.git)
   cd realtime-todo-api/django
   ```
Create and activate a virtual environment:
   

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
