""" Готов
Даны трехмерный тензор размерности X(n,k,k), состоящий из 0 или 1, или n картинок k*k. 
Нужно применить к нему указанную маску размерности (k,k). 
В случае, если биты в маске и картинке совпадают, то результирующий бит должен быть равен 0(False), иначе 1(True).
Получаем: FpF = F, FpT = T, TpF = T, TpT = F, Следовательно p = ^

P.S.: в заданиях про numpy прошу не использовать циклы python или их однострочные аналоги для генерации/создания списком, кортежей, словарей
"""

import numpy as np
from numpy.testing import assert_array_equal


def tensor_mask(X: np.ndarray, mask: np.ndarray) -> np.ndarray:
    ### ╰( ͡° ͜ʖ ͡° )つ──☆*:・ﾟ
    # ваш код

    return X ^ mask


######################################################
X = np.zeros(9, dtype=int).reshape((1, 3, 3))
mask = np.zeros(9, dtype=int).reshape((3, 3))
assert_array_equal(tensor_mask(X, mask), np.zeros(9, dtype=int).reshape((1, 3, 3)))
######################################################
X = np.ones(9, dtype=int).reshape((1, 3, 3))
mask = np.ones(9, dtype=int).reshape((3, 3))
assert_array_equal(tensor_mask(X, mask), np.zeros(9, dtype=int).reshape((1, 3, 3)))
######################################################
X = np.ones(9, dtype=int).reshape((1, 3, 3))
mask = np.zeros(9, dtype=int).reshape((3, 3))
assert_array_equal(tensor_mask(X, mask), np.ones(9, dtype=int).reshape((1, 3, 3)))
######################################################
X = np.zeros(9, dtype=int).reshape((1, 3, 3))
mask = np.ones(9, dtype=int).reshape((3, 3))
assert_array_equal(tensor_mask(X, mask), np.ones(9, dtype=int).reshape((1, 3, 3)))
######################################################
X = np.zeros(9 * 3, dtype=int).reshape((3, 3, 3))
mask = np.zeros(9, dtype=int).reshape((3, 3))
assert_array_equal(tensor_mask(X, mask), np.zeros(9 * 3, dtype=int).reshape((3, 3, 3)))
######################################################
X = np.ones(9 * 3, dtype=int).reshape((3, 3, 3))
mask = np.ones(9, dtype=int).reshape((3, 3))
assert_array_equal(tensor_mask(X, mask), np.zeros(9 * 3, dtype=int).reshape((3, 3, 3)))
######################################################
X = np.ones(9 * 3, dtype=int).reshape((3, 3, 3))
mask = np.zeros(9, dtype=int).reshape((3, 3))
assert_array_equal(tensor_mask(X, mask), np.ones(9 * 3, dtype=int).reshape((3, 3, 3)))
######################################################
X = np.zeros(9 * 3, dtype=int).reshape((3, 3, 3))
mask = np.ones(9, dtype=int).reshape((3, 3))
assert_array_equal(tensor_mask(X, mask), np.ones(9 * 3, dtype=int).reshape((3, 3, 3)))
######################################################
