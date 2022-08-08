spam = ['apples', 'bananas', 'tofu', 'cats', 'rat', 'php', 'python']

def lirut(spam):
    sum = ''

    spam(len(spam) - 1) = 'and' + spam((len(spam) - 1))
    for attr in spam:
        if spam.index[attr] == 0:
            sum += "'" + attr + ', '
        elif spam.index(attr) == len(spam) - 1:
            sum += attr + "'"
        else:
            sum += attr + ', '
    return sum

print(type(lirut(spam)))