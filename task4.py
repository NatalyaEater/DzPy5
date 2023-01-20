# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.


with open('task4one.txt', 'r') as file:
    text = file.readline()
    text_compression = text.split()

print(text)

def rle(a):
    enconding = ''
    prev_char = ''
    count = 1
    if not a:
        return ''
    for i in a:
        if i != prev_char:
            if prev_char:
                enconding += str(count) + prev_char
            count = 1
            prev_char = i
        else:
            count += 1
    else:
        enconding += str(count) + prev_char
        return enconding


text_compression = rle(text)

with open('task4two.txt', 'w', encoding='UTF-8') as file:
    file.write(f'{text_compression}')
print(text_compression)