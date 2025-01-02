# Задача 4

def print_users_as_table(users_to_print):
    width = 40
    header = f"{'ID'.center(width)}|{'Имя'.center(width)}|{'Фамилия'.center(width)}|{'Возраст'.center(width)}"
    print(header)
    print("=" * len(header))
    for i in users_to_print.keys():
        values = users_to_print.get(i)
        print(f"{i.center(width)}|{values[0].center(width)}|{values[1].center(width)}|{values[2].center(width)}")
        print()

users_from_input = dict()
while True:
        first_name = input('Введите имя (или нажмите Enter для завершения): ').capitalize()
        if not first_name:  # Проверка на пустую строку
            break
        if not first_name.isalpha():
            raise ValueError('Имя введено неверно')


        last_name = input('Введите фамилию: ').capitalize()
        if not last_name:
            raise ValueError(f'Для пользователя с именем {first_name} введены не все данные')

        age = input('Введите возраст: ')
        if not age:
            raise ValueError(f'Для пользователя с именем {first_name} введены не все данные')
        if not 18 <= int(age) <= 60:
            raise ValueError('возраст должен быть числом от 18 до 60')

        user_id = input('Введите ID: ').zfill(8)
        if not user_id:
            raise ValueError(f'Для пользователя с именем {first_name} введены не все данные')
        if not user_id.isdigit():
            raise ValueError('ID должен быть целым числом')
        if user_id in users_from_input:
            raise ValueError('ID должен быть уникальным')

        users_from_input[user_id] = (first_name, last_name, age)

print_users_as_table(users_from_input)