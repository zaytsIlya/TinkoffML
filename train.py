import random
import re

with open('obuchalka.txt', encoding='utf-8', mode='r') as f: #считываем файлы
    text = f.read()
#причнсываем текст
nice_text = re.split(r'\W+', text)
nice_text = [word.lower() for word in nice_text]
dictionary = set(nice_text)

counter1 = {}
counter2 = {}

#считаем биграмы и унииграмы
for i in range(0, len(nice_text) - 1):
    one = (nice_text[i])
    two = (nice_text[i], nice_text[i + 1])
    if one in counter1.keys():
        counter1[one] += 1
    else:
        counter1[one] = 1
    if two in counter2.keys():
        counter2[two] += 1
    else:
        counter2[two] = 1
dictionary.remove('')


def prediction(input_):
    c_input = input_.split()
    last_uni = str(c_input[-1])
    p = {}
    for word in dictionary:
        i_uni = last_uni
        i_bi = (last_uni, word)                 #сортируем по количеству повторений и делаем предсказания
        i_uni_counter = counter1.get(i_uni, 0)
        i_bi_counter = counter2.get(i_bi, 0)
        p[word] = i_bi_counter / i_uni_counter

    suggested_word_1 = max(p, key=p.get)
    p[suggested_word_1]= 0
    suggested_word_2 = max(p, key=p.get)       #чтобы не попадать в цикл, выбираем рандомно из топ 3 по популярности слов
    p[suggested_word_2]= 0
    suggested_word_3 = max(p, key=p.get)

    n = random.randrange(1, 3)
    if n == 1:
        return suggested_word_1
    elif n == 2:
        return suggested_word_2
    elif n == 3:
        return suggested_word_3
