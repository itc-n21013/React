def collatz(number):
    if number % 2 == 0:
        return int(number / 2)
    else:
        return int(3 * number + 1)

param = int(input("整数を入力してください:"))

while param != 1:
    param = collatz(param)
    print(param)
