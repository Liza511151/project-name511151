import pandas as pd
from sqlalchemy import create_engine
from src.etl import config

def load_data(df, table_name="liza511151"):
    print(f"Подключаюсь к БД и записываю {len(df)} строк...")

    # строка подключения
    db_url = f"postgresql+psycopg2://{config.DB_USER}:{config.DB_PASSWORD}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}"

    engine = create_engine(db_url)

    # встроенный метод Pandas для записи (как просил препод)
    df.to_sql(table_name, engine, if_exists='append', index=False)
    print("УСПЕХ! Данные записаны.")
