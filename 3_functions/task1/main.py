# Задача 1

snake_case_str = 'otus_course'
camel_case_str = 'PythonIsTheBest'
camel_snake_case_str = 'Camel_Snake_Case'

def convert_str_case(inputed: str):
    if '_' in inputed and inputed.islower():
        return ''.join(word.capitalize() for word in inputed.split('_'))
    elif inputed[0].isupper() and not '_' in inputed:
        return ''.join('_' + c.lower() if c.isupper() else c for c in inputed)[1:]
    else:
        return 'неверный формат строки'

print(convert_str_case(snake_case_str))
print(convert_str_case(camel_case_str))
print(convert_str_case(camel_snake_case_str))







