import json
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoProject.settings")
django.setup()
from steamdb.models import Info, GameName
from django.conf import settings

DATA_FILES_DIR = os.path.join(settings.BASE_DIR)

with open(os.path.join(DATA_FILES_DIR, 'Data.json'), 'r', encoding='utf-8') as f:
    data = json.load(f)
    ranks_data = data['ranks']

with open(os.path.join(DATA_FILES_DIR, 'GameName.json'), 'r', encoding='utf-8') as dataname_f:
    dataname = json.load(dataname_f)
    names_data = dataname['apps']

for rank_data in ranks_data:
    Info.objects.create(
        rank=rank_data['rank'],
        appid=rank_data['appid'],
        last_week_rank=rank_data['last_week_rank'],
        peak_in_game=rank_data['peak_in_game']
    )


for name_data in names_data:
    GameName.objects.create(
        appid=name_data['appid'],
        name=name_data['name']
    )

with open('GameName.json', 'r', encoding='UTF-8') as dataname_f:
    json.dump(GameName, dataname_f, ensure_ascii=False, indent=2)
