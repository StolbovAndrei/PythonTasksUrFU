# Создать декоратор my_saviour_decorator с "хорошим поведением", то есть
# декоратор при котором происходит сохранение "магических" полей name  и  doc

# Должны проходиться тесты, которые написаны с помощью ключевого слова assert

# Менять можно только код в my_saviour_decorator, который нужно создать самим.

# Использовать functools.wraps явно или неявно в этой задаче нельзя. По сути вам нужен его простой аналог.

# Не используйте, пожалуйста, в этом задании переменные и функции с именем wrapper или inner

# Подсказка: пройдитесь отладчиком или расставьте print, чтобы видеть как меняется,
# например, поле name у каждой (прям каждой) используемой функции, что содержися в аргументах, а
# my_simple_logging_decorator нужен, чтобы задача была менее тривиальной

def my_saviour_decorator(decorator_func):
    def my_decorator(main_function):
        decorated_function = decorator_func(main_function)

        decorated_function.__name__ = main_function.__name__
        decorated_function.__doc__ = main_function.__doc__


        return decorated_function


    return my_decorator


@my_saviour_decorator
def my_simple_logging_decorator(func):
    def you_will_never_see_this_name(*args, **kwargs):
        print(f"calling {func.__name__}")
        return func(*args, **kwargs)

    return you_will_never_see_this_name


@my_simple_logging_decorator
def double(x):
    "Doubles a number."
    return 2 * x


if __name__ == "__main__":
    assert double.__name__ == "double"
    assert double.__doc__ == "Doubles a number."
    # вывод для примера
    print(double(155))