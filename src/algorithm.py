from geopy.distance import geodesic
from scipy.optimize import linear_sum_assignment
import csv

cash_counter = 0
distance_counter = 0

#список заказов
order_list = []
with open('data/orders_data.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        row = [float(order) for order in row]
        order_list.append([(row[0], row[1]), (row[2], row[3]), int(row[4])])

#список курьеров
couriers_coordinate = []
with open('data/couriers_data.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        couriers_coordinate.append([float(courier) for courier in row])

#цикл для доставки всех заказов
counter = len(order_list)
while counter:

    #расстановка приоритетов
    couriers_priority = [[None for _ in range(len(order_list))] for _ in range(len(couriers_coordinate))]
    for i in range(len(couriers_coordinate)):
        for j in range(len(order_list)):
            couriers_priority[i][j] = geodesic(order_list[j][0], couriers_coordinate[i]).kilometers
    
    #назначение заказов по венгерскому алгоритму
    courier_index, order_index = linear_sum_assignment(couriers_priority)

    for r, c in zip(courier_index, order_index):
        distance = round(geodesic(order_list[c][0], couriers_coordinate[r]).kilometers, 2)
        price = order_list[c][2]
        print(f"курьеру {r+1} соответствует заказ {c+1} с расстоянием {distance} км и суммой {price} руб")
        couriers_coordinate[r] = order_list[c][1]
        distance_counter += distance
        cash_counter += price
    
    #для удаления доставленных заказов
    for i in sorted(order_index, reverse=True):
        order_list.pop(i)
    
    print()
    counter -= len(order_index)


print('Общая выручка:', cash_counter)
print(f'Пройденная дистанция: {round(distance_counter, 2)} км')
