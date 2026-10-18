from pathlib import Path

import requests
import pandas as pd


url = "https://jsonplaceholder.typicode.com/posts"

r = requests.get(url, timeout=15)
r.raise_for_status()
print("Статус:", r.status_code)

data = r.json()
print("Всего записей:", len(data))

# собираю строки
rows = []
for post in data:
    rows.append({
        "post_id": post["id"],
        "user_id": post["userId"],
        "title": post["title"],
        "body": post["body"],
        "title_length": len(post["title"]),
        "body_length": len(post["body"]),
    })

# превращаю в DataFrame pandas
df = pd.DataFrame(rows)

# путь сохранения — рядом со скриптом
script_dir = Path(__file__).parent
output_path = script_dir / "posts.csv"

# сохраняю
df.to_csv(output_path, index=False, encoding="utf-8-sig")
print("Сохранено в", output_path)

# вывожу таблицу вместо словарей
print("Первые 10 строк:")
print(df.head(10))
