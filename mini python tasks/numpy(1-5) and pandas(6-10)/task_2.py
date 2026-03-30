""" Готов
Дан одномерный массив целых чисел. Необходимо отсортировать в нем только числа, которые делятся на 2.
При этом начальный массив изменять нельзя.

P.S.: в заданиях про numpy прошу не использовать циклы python или их однострочные аналоги для генерации/создания списком, кортежей, словарей
"""

import numpy as np
from numpy.testing import assert_array_equal


def sort_evens(A: np.ndarray) -> np.ndarray:
    result = A.copy()

    is_even = result % 2 == 0
    even_numbers = result[is_even]
    sorted_even_numbers = np.sort(even_numbers)
    result[is_even] = sorted_even_numbers

    return result


A = np.array([43, 66, 34, 55, 78, 105, 2])
output = sort_evens(A)

######################################################
assert_array_equal(sort_evens(np.array([])), np.array([]))
######################################################
A1 = np.array([2, 0])
A2 = np.array([2, 0])
Ans = np.array([0, 2])
assert_array_equal(sort_evens(A1), Ans)
assert_array_equal(A1, A2)
######################################################
assert_array_equal(sort_evens(np.array([2, 0])), np.array([0, 2]))
######################################################
assert_array_equal(sort_evens(np.array([9, 3, 1, 5, 7])), np.array([9, 3, 1, 5, 7]))
######################################################
assert_array_equal(
    sort_evens(np.array([8, 12, 4, 10, 6, 2])), np.array([2, 4, 6, 8, 10, 12])
)
######################################################
assert_array_equal(
    sort_evens(np.array([8, 5, -4, -1, -10, 9])), np.array([-10, 5, -4, -1, 8, 9])
)
######################################################
assert_array_equal(
    sort_evens(np.array([43, 66, 34, 55, 78, 105, 2])),
    np.array([43, 2, 34, 55, 66, 105, 78]),
)
