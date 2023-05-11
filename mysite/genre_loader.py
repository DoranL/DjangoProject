import json
import os

currentPath = os.getcwd()
path = os.path.join(currentPath, 'genre.json')
with open(path, 'r', encoding='utf-8') as f:
    genre_list = json.load(f)

new_list = []
for genre in genre_list:
    new_data = {"model": "polls.genre"}
    new_data["fields"] = {}
    new_data["fields"]["name"] = genre
    new_list.append(new_data)

print(new_list)

with open('genre_data.json', 'w', encoding='UTF-8') as f:
    json.dump(new_list, f, ensure_ascii=False, indent=2)