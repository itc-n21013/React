#! python3
# lucky.py - Googleの検索結果をいくつか開く

import requests, sys, webbrowser, bs4

print('Gooling...')
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# TODO 上位の検索結果のリンクを取得する
soup = bs4.BeautifulSoup(res.text, 'lxml')

# TODO 各結果をブラウザのタブで開く
link_elems = soup.select('a.xeDNfc')
num_open = min(5, len(link_elems))
for i in range(num_open):
    webbrowser.open(link_elems[i].get('href'))