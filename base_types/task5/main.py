# Задача 5
try:
    input_data = float(input("введите данные: "))
    if input_data > 0:
        print(True)
    else:
        print(False)
except ValueError:
    print(False)