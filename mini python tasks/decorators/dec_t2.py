import functools


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Модифицируйте код декоратора prime_fizz_buzz_modificator
def prime_fizz_buzz_modificator(func):
    """Дан список целых чисел. Декоратор должен заменить каждое число в списке по следующим правилам (в порядке приоритета):

        Если число равно 42 → заменить на строку "Answer!" 
        Если число — простое → заменить на "Prime" 
        Если число составное и делится на 3 и на 5 → "FizzBuzz" 
        Если число составное и делится только на 3 → "Fizz" 
        Если число составное и делится только на 5 → "Buzz" 
        Во всех остальных случаях → оставить как есть.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        numbers_list = func(*args, **kwargs)
        result =[]

        for num in numbers_list:
            if num == 42:
                result.append("Answer!")
            elif is_prime(num):
                result.append("Prime")
            elif num % 3 == 0 and num % 5 == 0:
                result.append("FizzBuzz")
            elif num % 3 == 0:
                result.append("Fizz")
            elif num % 5 == 0:
                result.append("Buzz") 
            else:
                result.append(num)

        return result
    
    return wrapper


@prime_fizz_buzz_modificator
def numbers(from_num, to_num):
    return [num for num in range(from_num, to_num)]


if __name__ == "__main__":
    # вывод для примера
    print(numbers(from_num=2, to_num=20))
    print(numbers(from_num=40, to_num=45))


# Возможные вопросы к вашему решению (не полный список, для представления вариантов)

# Как вы определяете, является ли число простым? Почему число 1 не считается простым? Что вернёт ваша функция is_prime(1) и почему?
# Что произойдёт, если обернуть функцию, которая возвращает не список, а генератор? Нужно ли менять код декоратора? Почему?
# Зачем используется functools.wraps? Что изменится в поведении программы, если его убрать? Приведите пример (например, с help() или __name__).
# Представьте, что вы хотите добавить поддержку отрицательных чисел. Как изменится логика? Будут ли отрицательные числа когда-нибудь превращаться в "Fizz" или "Prime!"? Почему?
# Как вы протестировали бы свою функцию is_prime? Приведите 3–5 «крайних» случаев, которые важно проверить.
# Можно ли переписать логику замены чисел через словарь или цепочку функций? В чём плюсы и минусы такого подхода по сравнению с if-elif?
# Если вызвать декорированную функцию дважды — будет ли is_prime вызываться каждый раз для одних и тех же чисел? Как можно оптимизировать это (например, через кэширование)?