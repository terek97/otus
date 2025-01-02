# Задача 1

input_from_user = input("введите целое число: ")
if input_from_user.isdigit():

    while len(input_from_user) > 1:
            result = sum(int(i) for i in input_from_user)
            input_from_user = str(result)

    print(result)
else:
    print("Неверный формат ввода!")