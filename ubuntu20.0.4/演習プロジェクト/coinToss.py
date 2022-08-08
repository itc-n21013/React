import random
import logging
logging.basicConfig(level=logging.DEBUG,
format=' %(asctime)s - %(levelname)s - %(message)s')

guess = ' '
while guess not in ('表', '裏'):
    print('コインの表裏を当ててください。表か裏を入力してください:')
    guess = input()
toss = random.radint(0,1)
if guess == '表':
    guess = 0
else:
    guess = 1
logging.debug('toss = {}, guess = {}'.format(toss, guess))

if toss == guess:
    print('当たり！')
else:
    print('はずれ！もう一回当てて！')
    guess = input()

if guess == '裏':
    guess = 0
else:
    guess = 1
logging.debug('toss = {}, guess = {}'.format(toss, guess))

if toss == guess:
    print('当たり！')
else:
    print('はずれ。このゲームは苦手ですね。')