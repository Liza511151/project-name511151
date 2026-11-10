import argparse
from src.etl.extract import extract_data
from src.etl.transform import transform_data
from src.etl.load import load_data

def main():
    parser = argparse.ArgumentParser(description="ETL")
    parser.add_argument("--limit", type=int, default=100, help="кол-во строк")
    parser.add_argument("--file_id", type=str, default="1IGkNAXgYrcpQZ2feLChGal3Pu2UWN_Ll", help="айди файла")
    args = parser.parse_args()

    print(f"Старт. Лимит: {args.limit}")

    # 1. Загрузка
    df = extract_data(args.file_id)
    
    # 2. Обработка
    df = transform_data(df).head(args.limit)
    
    # 3. Запись
    load_data(df)
    print("Готово!")

if __name__ == '__main__':
    main()
