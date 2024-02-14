import csv

def promocod(arr):#функция для создания промокодов
    den, mes, god = arr[2].split('.')
    nazv = arr[1]
    return (nazv[:2] + den + nazv[-1] + nazv[-2] + mes[::-1]).upper()#вывод промокода

with open('products.csv', encoding='utf-8-sig') as file:
    data = list(csv.reader(file, delimiter=';'))#открытие и считывание файла
    with open('product_promo.csv', 'w', newline='', encoding='utf-8-sig') as new_file:#создание нового файла и его оформление
        writer = csv.DictWriter(new_file, delimiter=';', fieldnames=['category', 'product', 'date', 'price_per_unit', 'count', 'promocode'])
        writer.writeheader()
        for stat in data[1:]:
            newstat = {}#создание нового словаря, который после обработки будет является строчкой в новом файле
            newstat['category'] = stat[0]
            newstat['product'] = stat[1]
            newstat['date'] = stat[2]
            newstat['price_per_unit'] = stat[3]
            newstat['count'] = stat[4]
            newstat['promocode'] = promocod(stat)
            writer.writerow(newstat)#добовление словаря как строчку в файл
