#! python3
# quickWeather.py

import json, os, requests, sys, pprint
from pydoc import locate

# コマンドライン引数から地名を組み立てる

if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()
location = ' '.json(sys.argv[1:])

# openweathermap.orgから取得したAPIキーを定義しておく
APPID='f5351d228048a4e26401138dce69997f'

# TODO: OpenWeatherMap.orgのAPIからJSONデータをダウンロードする
# url = 'https://api.openweathermap.org/data/2.5/forecast/daily?q={}&cnt=3&appid={}'.format(location, APPID)
url = 'https://api.openweathermap.org/data/2.5/forecast/daily?q={}&cnt=3&appid={}'.format('35', '139', APPID)

response = requests.get(url)
response.raise_for_status()

# TODO: JSONデータからPython変数に読み込む
weather_data = json.loads(response.text)
# 天気予報の情報を表示する
weather = weather_data['weather'][0]
for k,v in weather.items():
    if k == 'main' or k == 'description':
        print(v)