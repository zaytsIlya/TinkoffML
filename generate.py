from train import dictionary
from train import prediction

print('введите слово')
word_given = input()
proverka = word_given.split()
while proverka[-1] not in dictionary:
    print('Такого слова в словаре нет, введите другое')     #защита от того, что слова нет в словаре
    word_given = input()
    proverka = word_given.split()


print('введите количество слов')
n = int(input())                                #задаем количество слов, которое предскажем

s = word_given
a = word_given
i = 0
while i < n:
    a = prediction(a)                          #выдаем предсказание
    s = s + ' ' + a
    i += 1
print(s)
