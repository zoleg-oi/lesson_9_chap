# Генераторы

def all_variants(text):
    n = 0
    t = ''
    for i in range(len(text)):
        for ii in range(len(text)):
            if i == 0:
                t = text[ii]
            else:
                t = text[ii:ii + i + 1]
            if len(t) >= i + 1:
                yield t


a = all_variants('abc')
for i in a:
    print(i)
