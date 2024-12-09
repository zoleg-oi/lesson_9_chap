# Генераторы

def all_variants(text):

    for i in range(len(text)):
        t = text[i]
        yield t
        for ii in range(i+1,len(text)):
            t += text[ii]
            yield t
a = all_variants('abc')

print(a)
for i in a:
    print(i)
