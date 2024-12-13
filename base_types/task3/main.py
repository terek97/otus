# Задача 3
try:
    length = int(input("Введите длину плитки: "))
    width = int(input("Введите ширину плитки: "))
    piece_size = int(input("Введите размер куска, который хотите отломить: "))

    if piece_size % length == 0 or piece_size % width == 0:
        print(True)
    else:
        print(False)
except ValueError:
    print("Неверный формат ввода!")

# P.S. не до конца ясно условие задачи, если логика неверная - прошу пояснить, что имелось ввиду


