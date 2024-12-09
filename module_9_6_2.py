# Генераторы

def all_variants(text):
    for i in range(len(text)):
        t = text[i]
        yield t
        for ii in range(i + 1, len(text)):
            t += text[ii]
            yield t


a = all_variants('abc')

print(a)
list_output = []
for i in a:
    list_output.append(i)
list_output.sort(key=len)
print(*list_output, sep='\n')
