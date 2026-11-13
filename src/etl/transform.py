import pandas as pd

def transform_data(df):
    df = df.copy()

    # Проверяем, что все нужные колонки есть
    required_cols = ["Mixing_Temperature", "Viscosity_cP", "pH", "Stability_Days"]
    for col in required_cols:
        if col not in df.columns:
            raise KeyError(f"Нет нужной колонки: {col}")

    # чистим и приводим типы
    df["Mixing_Temperature"] = df["Mixing_Temperature"].str.extract(r"(\d+)").astype(float)
    df["Viscosity_cP"] = pd.to_numeric(df["Viscosity_cP"], errors="coerce")
    df["pH"] = pd.to_numeric(df["pH"], errors="coerce")
    df["Stability_Days"] = pd.to_numeric(df["Stability_Days"], errors="coerce").astype("Int64")

    # мои данные
    df['surname'] = 'Антипова'
    df['name'] = 'Елизавета'
    df['patronymic'] = 'Игоревна'

   # Приводим названия колонок к нижнему регистру для БД
    df.columns = df.columns.str.lower()
   
    # None для базы
    df = df.where(pd.notnull(df), None)
    return df
