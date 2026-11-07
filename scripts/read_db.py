import os
import psycopg2
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

try:
    conn = psycopg2.connect(
        host=DB_HOST, port=DB_PORT, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD
    )
    cursor = conn.cursor()

    # Смотрим, кто мы
    cursor.execute("SELECT current_user;")
    print("Мы подключены как:", cursor.fetchone()[0])

    # Пытаемся создать свою таблицу (назовем её по твоему логину)
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS liza511151 (
                batch_id VARCHAR(50),
                formula_type VARCHAR(50),
                mixing_temperature VARCHAR(50),
                viscosity_cp FLOAT,
                ph FLOAT,
                stability_days INT,
                surname VARCHAR(50),
                name VARCHAR(50),
                patronymic VARCHAR(50)
            );
        """)
        conn.commit()
        print("УСПЕХ: Таблица 'liza511151' успешно создана (или уже существовала)!")
    except Exception as create_err:
        print("Не удалось создать таблицу:", create_err)
        conn.rollback()

    cursor.close()
    conn.close()
except Exception as e:
    print("ОШИБКА подключения:", e)
