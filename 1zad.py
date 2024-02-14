import csv

it_summa_zak = 0#суммарная сумма закусок
with open('products.csv', encoding='utf-8-sig') as file:
    data = list(csv.DictReader(file, delimiter=';'))#открытие и считывание файла
    with open('products_new.csv', 'w', newline='', encoding='utf-8-sig') as new_file:#создание нового файла и его оформление
        writer = csv.DictWriter(new_file, delimiter=';', fieldnames=['category', 'product', 'date', 'price_per_unit', 'count', 'total'])
        writer.writeheader()
        for stat in data:
            if stat['Category'] == 'Закуски':
                it_summa_zak += int(stat['Price_per_unit'][:-2]) * int(stat['Count'][:-2])#закидываем в переменную сумму всех закусок
            newstat = {}#создание нового словаря, который после обработки будет является строчкой в новом файле
            newstat['category'] = stat['Category']
            newstat['product'] = stat['product']
            newstat['date'] = stat['Date']
            newstat['price_per_unit'] = stat['Price_per_unit']
            newstat['count'] = stat['Count']
            newstat['total'] = int(stat['Price_per_unit'][:-2]) * int(stat['Count'][:-2])
            writer.writerow(newstat)#добовление словаря как строчку в файл
print(it_summa_zak)#вывод суммы


