# Задача 2
try:
    days_till_vacation = int(input("Сколько дней вам осталось до ближайшего отпуска? "))
    full_weeks = days_till_vacation // 7
    add_weekends = 1 if days_till_vacation % 7 == 6 else 0

    result = full_weeks * 2 + add_weekends

    print("количество выходных дней до отпуска: ", result)
except ValueError:
    print("Неверный формат ввода!")
