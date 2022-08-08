import re

def validatePassword(string):
    if len(string) >= 8:
        regex = re.compile(r'[A-Z]+')
        regex2 = re.compile(r'[a-z]+')
        regex3 = re.compile(r'\d+')

        if regex.search(string) == None:
            return '大文字を使用してください。'

        if regex2.search(string) == None:
            return '少文字を使用してください'

        if regex3.search(string) == None:
            return '数字を1以上使用してください。'

        return 'バリデーションが完了しました。'

    else:
        return '文字数は8文字以上にしてください。'

print('パスワードを入力してください。')
input_text = input()
print(validatePassword(input_text))
