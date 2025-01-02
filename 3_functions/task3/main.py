# Задача 3
from math import sqrt

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            return False
    return True

print(is_prime(17))
print(is_prime(20))
print(is_prime(23))
