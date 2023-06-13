import json
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoProject.settings")
django.setup()
from steamdb.models import Rank, App
from django.db import connection
from django.conf import settings

DATA_FILES_DIR = os.path.join(settings.BASE_DIR)

with open(os.path.join(DATA_FILES_DIR, 'Data.json'), 'r', encoding='utf-8') as f:
    data = json.load(f)
    ranks_data = data['ranks']

with open(os.path.join(DATA_FILES_DIR, 'GameName.json'), 'r', encoding='utf-8') as dataname_f:
    dataname = json.load(dataname_f)
    names_data = dataname['applist']['apps']

# 데이터 삭제
with connection.cursor() as cursor:
    cursor.execute("DELETE FROM rank")
    cursor.execute("DELETE FROM app")

# 정보 테이블 생성
objects = [App(id=data['appid'], name=data['name']) for data in names_data]
App.objects.bulk_create(objects)

# 순위 테이블 생성
for data in ranks_data:
    Rank.objects.create(
        rank=data['rank'],
        app_id=data['appid'],
        last_week_rank=data['last_week_rank'],
        peak_in_game=data['peak_in_game']
    )

print('-----Data Saved')