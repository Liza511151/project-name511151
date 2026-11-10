import os
import gdown
import zipfile
import pandas as pd

def extract_data(file_id, zip_path="archive.zip", data_dir="data"):
    # скачиваем если нет
    if not os.path.exists(zip_path):
        print("Скачиваю...")
        gdown.download(id=file_id, output=zip_path, quiet=False)
    # распаковка
    print("Распаковываю zip...")
    with zipfile.ZipFile(zip_path, "r") as z:
        z.extractall(data_dir)

    # ищем нужный файл
    csv_path = None
    for root, _, files in os.walk(data_dir):
        for name in files:
            if name.endswith(".csv"):
                csv_path = os.path.join(root, name)
                break

    if csv_path is None:
        raise FileNotFoundError("Не нашел csv в архиве")
        
    return pd.read_csv(csv_path)
       