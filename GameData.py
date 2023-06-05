import json
import time

import requests
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
def add_table(key):
    url = f"https://store.steampowered.com/api/appdetails?appids={key}&l=korean"  # JSON 파일의 URL
    response = requests.get(url)  # GET 요청 보내기
    if response.status_code == 200:  # 요청이 성공한 경우
        data = response.json()  # JSON 데이터 파싱
        # 데이터 처리 작업 수행
        try:
            if data[str(key)]['data']['type'] == "game":
                if data[str(key)]['data']['is_free'] == "True":
                    App.objects.create(
                        id=key,
                        name=data[str(key)]['data']['name'],
                        header_image=data[str(key)]['data']['header_image'],
                        capsule_image=data[str(key)]['data']['capsule_image'],
                        is_free=data[str(key)]['data']['is_free'],
                    )
                else:
                    App.objects.create(
                        id=key,
                        name=data[str(key)]['data']['name'],
                        header_image=data[str(key)]['data']['header_image'],
                        capsule_image=data[str(key)]['data']['capsule_image'],
                        is_free=data[str(key)]['data']['is_free'],
                        initial_price=str(data[str(key)]['data']['price_overview']['initial'])[:-2],
                        final_price=str(data[str(key)]['data']['price_overview']['final'])[:-2],
                        discount_percent=data[str(key)]['data']['price_overview']['discount_percent'],
                    )
                print(f"{key} 추가 완료")
            else:
                raise Exception("'타입'(이)가 '게임'(이)가 아님")
        except Exception as e:
            print(f"{key} 추가 실패:", e)
        return True
    else:
        print(f"{key} 요청 실패:", response.status_code)
        return False


# 요청을 실패했을 경우, 다시 반복
for app in names_data:
    while True:
        if add_table(app['appid']):
            break
        time.sleep(300)

# 순위 테이블 생성
for data in ranks_data:
    Rank.objects.create(
        rank=data['rank'],
        app_id=data['appid'],
        last_week_rank=data['last_week_rank'],
        peak_in_game=data['peak_in_game']
    )

print('Data Saved')
