import csv

with open('products.csv', encoding='utf-8-sig') as file:
    data = list(csv.DictReader(file, delimiter=';'))#открытие и считывание файла
    vvod = input()#создание переменной, которая будет отвечать за ввод
    minimum = float('inf')
    minimum_product = ''#переменные для нахождения минимума
    while vvod != 'молоко':#условия для остановки программы
        for stat in data:
            if stat['Category'] == vvod:
                if int(stat['Count'][:-2]) < minimum:#алгоритм нахождения минимума в заданной категории
                    minimum = int(stat['Count'][:-2])
                    minimum_product = stat['product']
        if minimum == float('inf'):
            print('Такой категории не существует в нашей БД')#вывод если категории нет
        else:
            print(f'В категории: {vvod} товар: {minimum_product} был куплен {minimum} раз')#вывод тесли категория есть
        vvod = input()