import psycopg2
import pandas as pd

DB_HOST = "85.193.80.59"
DB_PORT = "5432"
DB_NAME = "homeworks"
DB_USER = "deexpert"
DB_PASSWORD = "what_a_Wonderful_Day!"

def main():
    print("Читаю датасет...")
    # Читаем 100 строк
    df = pd.read_csv("data/cosmetic_process_optimisation.csv").head(100)
    
    # Добавляем ФИО
    df['surname'] = 'Антипова'
    df['name'] = 'Елизавета'
    df['patronymic'] = 'Игоревна'
    
    # Меняем NaN на None
    df = df.where(pd.notnull(df), None)

    print("Подключаюсь к базе данных...")
    try:
        conn = psycopg2.connect(
            host=DB_HOST, port=DB_PORT, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD
        )
        cursor = conn.cursor()
        
        # Формируем запрос к нашей новой таблице
        cols_to_insert = list(df.columns)
        placeholders = ','.join(['%s'] * len(cols_to_insert))
        query = f"INSERT INTO liza511151 ({','.join(cols_to_insert)}) VALUES ({placeholders})"

        records = df.values.tolist()

        print(f"Записываю {len(records)} строк в таблицу liza511151...")
        cursor.executemany(query, records)
        
        conn.commit() # Сохраняем
        print("УСПЕХ! Данные успешно записаны.")
        
        cursor.close()
        conn.close()
        
    except Exception as e:
        print("ОШИБКА при записи:", e)

if __name__ == '__main__':
    main()
