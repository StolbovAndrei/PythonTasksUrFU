import functools
import re

# Модифицируйте код декоратора reverse_string
"""Модифицируйте декоратор reverse_string так, чтобы он:

    Проверял, является ли результат функции строкой.
    Если это строка, используя регулярные выражения, 
    извлекал из неё только буквенные символы и пробелы (удаляя цифры, знаки препинания и т.д.).
    Затем переворачивал очищенную строку.
    Если результат не строка — возвращал None.
    """

def reverse_string(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        
        if not isinstance(result, str):
            return None
        
        filtered_string = re.sub(r'[^a-zA-Zа-яА-ЯёЁ\s]', '', result)
        
        return filtered_string[::-1]
    
    return wrapper

    


@reverse_string
def get_university_name():
    return "Western Institute of Technology and Higher Education"


@reverse_string
def get_university_founding_year():
    return 1957

@reverse_string
def get_messy_name():
    return "Western Institute, est. 1957! @#$"


if __name__ == "__main__":
    # вывод для примера
    print(get_university_name(), get_university_founding_year(), get_messy_name(), sep="\n")

    # Задача моделирует реальную потребность — обработка "грязных" данных, 
    # когда нужно извлечь чистый текст перед дальнейшей обработкой.