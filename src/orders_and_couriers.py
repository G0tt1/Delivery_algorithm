from random import uniform, randint
import csv

order_list = []
couriers_coordinate = []
orders_filename = 'data/orders_data.csv'
couriers_filename = 'data/couriers_data.csv'

for _ in range(int(input('Укажите количество заказов: '))):
    coordinate_Ax = uniform(61.93, 62.12)
    coordinate_Ay = uniform(129.55, 129.85)
    coordinate_Bx = uniform(61.93, 62.12)
    coordinate_By = uniform(129.55, 129.85)
    total_pay = randint(20, 50) * 10
    order_list.append((coordinate_Ax, coordinate_Ay, coordinate_Bx, coordinate_By, total_pay))

for _ in range(int(input('Укажите количество курьеров: '))):
    couriers_coordinate.append((uniform(61.93, 62.12), uniform(129.55, 129.85)))

with open(orders_filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(order_list)

with open(couriers_filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(couriers_coordinate)

print('Файлы успешно созданы')
