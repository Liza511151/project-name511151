import csv
from pathlib import Path

import requests


url = "https://jsonplaceholder.typicode.com/posts"

r = requests.get(url, timeout=15)
r.raise_for_status()  # упадёт с понятной ошибкой, если не 200
print("Статус:", r.status_code)

data = r.json()
print("Всего записей:", len(data))

# собираю строки для датасета
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

# путь к папке, где лежит скрипт
script_dir = Path(__file__).parent
output_path = script_dir / "posts.csv"

# сохраняю в csv
with open(output_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=["post_id", "user_id", "title", "body", "title_length", "body_length"],
    )
    writer.writeheader()
    writer.writerows(rows)

print("Сохранено в", output_path)
print("Первые 10 строк:")
for row in rows[:10]:
    print(row)
