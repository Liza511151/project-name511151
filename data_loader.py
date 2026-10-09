import gdown
import zipfile
import os
import pandas as pd


def find_csv(directory):
    """Находит первый CSV-файл в папке (включая вложенные)."""
    for root, _, files in os.walk(directory):
        for name in files:
            if name.endswith(".csv"):
                return os.path.join(root, name)
    return None


def load_data():
    """Скачивает архив с Google Drive, распаковывает и читает CSV в DataFrame."""
    file_id = "1IGkNAXgYrcpQZ2feLChGal3Pu2UWN_Ll"
    zip_path = "archive.zip"
    data_dir = "data"

    if not os.path.exists(zip_path):
        print("Скачиваю архив...")
        try:
            gdown.download(id=file_id, output=zip_path, quiet=False)
        except gdown.errors.DownloadError as e:
            print("Не удалось скачать архив:", e)
            return None
    else:
        print("Архив уже скачан, пропускаю загрузку.")

    print("Распаковываю архив...")
    try:
        with zipfile.ZipFile(zip_path, "r") as z:
            z.extractall(data_dir)
    except zipfile.BadZipFile:
        print("Архив повреждён или это не zip-файл.")
        return None

    csv_path = find_csv(data_dir)
    if csv_path is None:
        print("CSV-файл не найден в архиве.")
        return None
    print("Найден CSV:", csv_path)

    df = pd.read_csv(csv_path)
    return df


def cast_types(df):
    """Приводит типы столбцов к правильным."""
    df = df.copy()

    # Числовые столбцы
    df["Viscosity_cP"] = pd.to_numeric(df["Viscosity_cP"], errors="coerce")
    df["pH"] = pd.to_numeric(df["pH"], errors="coerce")
    df["Stability_Days"] = pd.to_numeric(df["Stability_Days"], errors="coerce").astype("Int64")

    # Mixing_Temperature: "High_60C" → 60.0, "Low_35C" → 35.0
    df["Mixing_Temperature"] = (
        df["Mixing_Temperature"].str.extract(r"(\d+)").astype(float)
    )

    # Formula_Type — категория
    df["Formula_Type"] = df["Formula_Type"].astype("category")

    # Batch_ID — строка
    df["Batch_ID"] = df["Batch_ID"].astype("string")
    return df


def save_parquet(df, path="cosmetic.parquet"):
    """Сохраняет DataFrame в формат .parquet."""
    df.to_parquet(path, index=False)
    print("Сохранено в", path)


if __name__ == '__main__':
    df = load_data()
    if df is None:
        raise SystemExit("Не удалось загрузить данные.")

    print("\n--- Типы ДО приведения ---")
    print(df.dtypes)

    df = cast_types(df)

    print("\n--- Типы ПОСЛЕ приведения ---")
    print(df.dtypes)

    print("\n--- Первые 10 строк ---")
    print(df.head(10))

    save_parquet(df)
