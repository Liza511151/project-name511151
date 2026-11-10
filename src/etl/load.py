import pandas as pd
from sqlalchemy import create_engine
from src.etl import config

def load_data(df, table_name="liza511151"):
    print(f"Подключаюсь к БД и записываю {len(df)} строк...")
    
    # Безопасная передача параметров (без склейки URL)
    engine = create_engine(
        "postgresql+psycopg2://",
        connect_args={
            "host": config.DB_HOST,
            "port": config.DB_PORT,
            "dbname": config.DB_NAME,
            "user": config.DB_USER,
            "password": config.DB_PASSWORD
        }
    )
    
    # Встроенный метод Pandas для записи
    df.to_sql(table_name, engine, if_exists='append', index=False)
    print("УСПЕХ! Данные записаны.")
