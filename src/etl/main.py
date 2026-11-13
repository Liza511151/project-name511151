import argparse
import logging
from src.etl.extract import extract_data
from src.etl.transform import transform_data
from src.etl.load import load_data

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def main():
    parser = argparse.ArgumentParser(description="ETL")
    parser.add_argument("--limit", type=int, default=100, help="кол-во строк")
    parser.add_argument("--file_id", type=str, default="1IGkNAXgYrcpQZ2feLChGal3Pu2UWN_Ll", help="айди файла")
    args = parser.parse_args()

    # Проверка, что лимит положительный
    if args.limit <= 0:
        parser.error("--limit должен быть положительным")

    logging.info(f"Старт. Лимит: {args.limit}")
    
    # 1. Загрузка
    df = extract_data(args.file_id)
    logging.info(f"Извлечено {len(df)} строк")
    
    # 2. Обработка
    df = transform_data(df).head(args.limit)
    
    # 3. Запись
    load_data(df)
    logging.info("Готово!")

if __name__ == '__main__':
    main()
