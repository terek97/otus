# Задача 4

roman_nums = {
    1: 'I',
    4: 'IV',
    5: 'V',
    9: 'IX',
    10: 'X',
    40: 'XL',
    50: 'L',
    90: 'XC',
    100: 'C',
    400: 'CD',
    500: 'D',
    900: 'CM',
    1000: 'M'
}

def convert(number):
    result = []

    while number > 0:
        closest_less_num = max(key for key in roman_nums.keys() if key <= number)
        result.append(roman_nums[closest_less_num])
        number -= closest_less_num

    return ''.join(result)

try:
    arabic_num = int(input('Введите целое положительное число: '))
    print('Результат конвертации в римское число: ' + convert(arabic_num))
except ValueError:
    print('Неверный формат ввода!')
