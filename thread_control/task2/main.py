# Задача 2
# Считаем, что 0 - это свободное место

import ast

cinema_rows_input = input("Введите данные в формате: [[1, 0, 1], [1, 1, 1], [0, 0, 0]]: ")
count_of_tickets = input("Введите необходимое кол-во билетов: ")

def get_first_row_with_enough_seats(cinema_rows):
    for row_number, row in enumerate(cinema_rows):
        count_of_nearby_seats = 0
        for seat in row:
            count_of_nearby_seats = 0 if seat else count_of_nearby_seats + 1
            if count_of_nearby_seats >= int(count_of_tickets):
                return row_number
    return 'False'

try:
    result = False
    print(get_first_row_with_enough_seats(ast.literal_eval(cinema_rows_input)))
except ValueError:
    print("Неверный формат ввода!")