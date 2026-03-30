""" Готов
На вход подается np.ndarray c натуральными числами. Надо получить массив сумм цифр в этих числах.

P.S.: в заданиях про numpy прошу не использовать циклы python или их однострочные аналоги для генерации/создания списком, кортежей, словарей
"""


import numpy as np
from numpy.testing import assert_array_equal


# def sum_of_digits(x):
#     str_x = str(x)
#     total = 0
#     for digit_char in str_x:
#         total += int(digit_char)
#     return total

def num_sum(a: np.ndarray) -> np.ndarray:
    ### ╰( ͡° ͜ʖ ͡° )つ──☆*:・ﾟ
    
    return np.vectorize(lambda x: sum(int(d) for d in str(x)))(a)


######################################################
assert_array_equal(num_sum(np.array([82])), np.array([10]))
######################################################
assert_array_equal(num_sum(np.array([1241, 354, 121])), np.array([8, 12, 4]))
######################################################
assert_array_equal(num_sum(np.array([1, 22, 333, 4444, 55555])), np.array([1, 4, 9, 16, 25]))
######################################################
