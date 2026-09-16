f = input("ФИО: ")
words = f.split()
i = ""
for word in words:
    i += word[0].upper()
h = " ".join(words)
l = len(h)
print(f'Инициалы: {i}.')
print(f'Длина: {l}')

