import psycopg2

DB_HOST = "85.193.80.59"
DB_PORT = "5432"
DB_NAME = "homeworks"
DB_USER = "deexpert"
DB_PASSWORD = "what_a_Wonderful_Day!"

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
