import gdown
import zipfile
import csv
import os


def load_data():
    file_id = "1IGkNAXgYrcpQZ2feLChGal3Pu2UWN_Ll"

    
    print("Начинаю скачивание...")
    zip_path = gdown.download(id=file_id, output="archive.zip", quiet=False)
    print("Скачан архив:", zip_path)

    
    with zipfile.ZipFile(zip_path, "r") as z:
        z.extractall("data")
    print("Содержимое архива:", os.listdir("data"))

   
    csv_path = os.path.join("data", "cosmetic_process_optimisation.csv")
    print("Читаю файл:", csv_path)

    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            print(row)
            if i == 9:
                break


if __name__ == '__main__':
    load_data()