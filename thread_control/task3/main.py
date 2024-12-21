# Задача 3

input_from_user = input("введите строку: ")

count_of_current_char = 1
length = len(input_from_user)

for i in range(length):
    letter = input_from_user[i]
    if letter != ' ':
        if i != length - 1 and letter == input_from_user[i+1]:
            count_of_current_char += 1
        else:
            print(str(count_of_current_char) + letter)
            count_of_current_char = 1