#! python3
# stopwatch.py

import time

# プログラムの説明を表示する
print('Enterを押すと開始します。その後、Enterを押せば経過時間を表示します。Ctrl-Cで終了します。')
input() # Enterを押すと開始
print('スタート')
start_time = time.time() #プログラムと最初のラップの開始時間
last_time = start_time

lap_num = 1

# TODO: ラップタイムを計測する
try:
    while True:
        input()
        now = time.time()
        lap_time = round(now - last_time, 2)
        total_time = round(now - start_time, 2)
        print('ラップ #{}: {} ({})'.format(lap_num, total_time, lap_time), end='')
        lap_num += 1
        last_time = now # ラップタイムをリセット
except KeyboardInterrupt:
    # Ctrl-C例外を処理してエラーメッセージを表示しないようにする
    print('\n終了.')