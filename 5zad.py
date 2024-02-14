import csv

def hashh(strk):#функция для создания хэша
    p = 71
    m = 10**9 + 9#это консатны для формулы
    alf = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ, '#алфавит
    hash = 0
    slovarik = {alf[i]: i + 1 for i in range(len(alf))}
    for i in range(len(strk)):
        hash += slovarik[strk[i]] * (i + 1) ** 2
    hash *= (p**len(strk) - 1)
    hash += p
    return hash % m#вывод хэша через формулу

with open('products.csv', encoding='utf-8-sig') as file:
    data = list(csv.DictReader(file, delimiter=';'))#открытие и считывание файла
    with open('product_hash.csv', 'w', newline='', encoding='utf-8-sig') as new_file:#создание нового файла с хэш таблицей и его оформление
        writer = csv.DictWriter(new_file, delimiter=';', fieldnames=['hash', 'count'])
        writer.writeheader()
        for stat in data:
            newstrk = {}#создание нового словаря, который после обработки будет является строчкой в новом файле
            newstrk['hash'] = hashh(stat['Category'])
            newstrk['count'] = stat['Count']
            writer.writerow(newstrk)#добовление словаря как строчку в файл
with open('products.csv', encoding='utf-8-sig') as file:
    data_spisok = list(csv.reader(file, delimiter=';'))#открытие и считывание файла но уже как список а не словарь
    data_spisok.sort(key=lambda spis: spis[-1])
    spisok_naimensih = []#список в котором будут хранится продукты с наименьшей продажей
    schetcik = 0#счетчик для формулы
    while len(spisok_naimensih) < 10:
        spisok_naimensih.append([data_spisok[schetcik][0], data_spisok[schetcik][-1]])#добавление 10 элементов в наш список
        schetcik += 1
    print(spisok_naimensih)#вывод нужного нам списка

