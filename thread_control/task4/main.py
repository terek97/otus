# Задача 4

try:
    strToEncrypt = input('Введите строку: ')
    shift = int(input('Введите ключ шифра (сдвиг): ')) % 26
    result = ''

    for i in strToEncrypt:
        if i.isalpha():
            currentIndex = ord(i.lower()) - ord('a')
            if shift > 25 - currentIndex:
                currentShift = shift - (25 - currentIndex) - 1
                currentIndex = 0
            newLetter = chr(ord('a') + currentIndex + shift)
            result += newLetter if i.islower() else newLetter.upper()
        # uncomment if it's necessary to leave not isalpha symbols as they are
        # else:
        #     result += i
    print(result)
except ValueError:
    print('Неверный формат ввода!')
