import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# Проверка переменных с выводом конкретных пропусков
required = {
    "DB_HOST": DB_HOST,
    "DB_PORT": DB_PORT,
    "DB_NAME": DB_NAME,
    "DB_USER": DB_USER,
    "DB_PASSWORD": DB_PASSWORD
}

missing = [name for name, val in required.items() if not val]

if missing:
    raise RuntimeError(f"Не заданы переменные: {', '.join(missing)}. Проверьте .env")

# Проверка, что порт — это число
try:
    int(DB_PORT)
except ValueError:
    raise RuntimeError(f"DB_PORT должен быть числом, а не '{DB_PORT}'")
