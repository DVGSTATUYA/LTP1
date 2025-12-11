# LTP1

REST API для загрузки и работы с производственными таблицами мебельной фабрики.

## 📦 Стек технологий

- Python 3.11+
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic v2
- Uvicorn
- python-dotenv

## 📁 Структура проекта
<img width="302" height="552" alt="image" src="https://github.com/user-attachments/assets/890f0125-e2f9-4e6b-b78e-d9fa7d55de69" />


## 🚀 Запуск проекта с нуля

1. Клонировать репозиторий
git clone <repo-url>
cd furniture-api

Или
Скачать папку furniture-api

2. Создать и активировать виртуальное окружение
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/macOS

3. Установить зависимости
pip install -r requirements.txt

4. Запустить сервер
uvicorn app.main:app --reload

5. Открыть документацию

Swagger UI: http://localhost:8000/docs
ReDoc: http://localhost:8000/redoc
