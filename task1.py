# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

print('Введите текст через запятую:')
textone = input()
print('Вид исходного текста:')
print(textone)

chance= "абв"
texttwo = [i for i in textone.split(',') if chance not in i]

print('Вид исправленного текста:')
print(texttwo)