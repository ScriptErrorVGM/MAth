import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

while True:
    print('Выберите действие:\n  1: Добавить вершину\n  2: Добавить ребро\n  0: Завершить')
    choice = int(input('Ваш выбор: '))
    if choice == 1:
        value = int(input('Введите значение для новой вершины: '))
        G.add_node(value)
    elif choice == 2:
        value1 = int(input('Введите первое значение нового ребра: '))
        value2 = int(input('Введите второе значение нового ребра: '))
        G.add_edge(value1, value2)
    elif choice == 0:
        break
    else:
        print('Неверный выбор, попробуйте снова.\n')

