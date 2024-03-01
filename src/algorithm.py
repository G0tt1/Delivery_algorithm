from geopy.distance import geodesic
from scipy.optimize import linear_sum_assignment
import csv
import os

cash_counter = 0
distance = 0

#список заказов
order_list = []
with open('src/data/orders_data.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        row = [float(order) for order in row]
        order_list.append([(row[0], row[1]), (row[2], row[3]), int(row[4])])

#список курьеров
couriers_coordinate = []
with open('src/data/couriers_data.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        couriers_coordinate.append([float(courier) for courier in row])

couriers_priority = [[None for _ in range(len(order_list))] for _ in range(len(couriers_coordinate))]
for i in range(len(couriers_coordinate)):
    for j in range(len(order_list)):
        couriers_priority[i][j] = geodesic(order_list[j][0], couriers_coordinate[i]).kilometers

courier_index, order_index = linear_sum_assignment(couriers_priority)

for r, c in zip(courier_index, order_index):
    print(f"курьеру {r+1} соответствует заказ {c+1}")


# counter = len(order_index)
# counter_order = len(order_list)
# while counter != len(order_list):
#     for i in range(len(couriers_coordinate)):
#         couriers_coordinate[i] = order_list[order_index[i]][1]
    
# print(*couriers_coordinate, sep='\n')