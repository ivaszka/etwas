"""Скопировать из файла F1 в файл F2 строки, начиная с четвертой по порядку. Подсчитать количество
символов в последнем слове F2."""

poem = open("poem", "w", encoding='utf-8')
lines = ["На золотом крыльце сидели\n",
         "царь царевич, король королевич\n",
         "сапожник, портной\n",
         "кто ты будешь такой?\n",
         "говори поскорей,\n",
         "не задерживай честных и добрых людей\n"]
poem.writelines(lines)
poem.close()
poem = open("poem", "r", encoding='utf-8')
result = open("result", "w", encoding='utf-8')
a = 0
while True:
    line = poem.readline()
    if not line:
        break
    if a >= 3:
        result.write(line)
    a += 1
result.close()
result = open("result", "r", encoding='utf-8')
line1 = ''
while True:
    line = result.readline()
    if not line:
        break
    line1 = line
result.close()
words = line1.split()
last_word = words[len(words)-1]
print('number of characters in the word "' + last_word + '" is', len(last_word))
