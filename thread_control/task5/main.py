# Задача 5

records = {}

try:
    while True:
        input_from_user = input("Введите строку в формате: 'название предмета' 'фамилия ученика' 'оценка' (или нажмите Enter для завершения): ")
        if not input_from_user:
            break

        subject, student, grade = input_from_user.split()

        if subject not in records:
            records[subject] = {}
        if student not in records[subject]:
            records[subject][student] = []

        records[subject][student].append(grade)

    for subject, students in records.items():
        print(subject)
        for student, grades in students.items():
            print(student + " " + (' '.join(grades)))
        print()
except ValueError:
    print('Неверный формат ввода!')