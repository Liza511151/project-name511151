import requests
import csv


url = "https://jsonplaceholder.typicode.com/posts"

r = requests.get(url, timeout=15)
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

# сохраняю в csv
with open("posts.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print("Сохранено в posts.csv")
print("Первые 10 строк:")
for row in rows[:10]:
    print(row)
