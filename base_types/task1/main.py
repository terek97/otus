# Задача 1
a = input("введите пятизначное число: ")
if len(a) == 5 and a.isdigit():
    print("Результат: " + a[0:1] + a[3:0:-1] + a[-1:])
else:
    print("Неверный формат ввода!")