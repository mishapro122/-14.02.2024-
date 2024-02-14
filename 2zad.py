import csv

with open('products.csv', encoding='utf-8-sig') as file:
    data_spisok = list(csv.reader(file, delimiter=';'))#открытие и считывание файла
    data_spisok.sort(key=lambda spis: spis[0])#сортировка списка по категориям
    maxprice = 0
    maxproduct = ''#создание переменных для нахождения максимума
    for stat in data_spisok[1:]:
        if stat[0] != 'Выпечка':
            break
        if int(stat[-2][:-2]) > maxprice:
            maxprice = int(stat[-2][:-2])#алгоритм нахождения максимума
            maxproduct = stat[1]
    print(f'В категории: Выпечка самый дорогой товар: {maxproduct} его цена за единицу товара составляет {maxprice}')#вывод необходимой нам информации



