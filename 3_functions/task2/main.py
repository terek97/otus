# Задача 2
from datetime import datetime

def check_date_valid(date):
    try:
        datetime.strptime(date, "%d.%m.%Y")
        return True
    except ValueError:
        return False


print(check_date_valid('29.02.2000'))
print(check_date_valid('29.02.2001'))
print(check_date_valid('31.04.1962'))