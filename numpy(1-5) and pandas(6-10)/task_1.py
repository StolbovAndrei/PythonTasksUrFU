""" Готов
Реализуйте функцию, принимающую на вход непустой тензор (может быть многомерным)
и некоторое число
и возвращающую ближайший к числу элемент тензора. Если ближайших несколько - выведите минимальный из ближайших.
(Вернуть нужно само число, а не индекс числа!)

P.S.: в заданиях про numpy прошу не использовать циклы python или их однострочные аналоги для генерации/создания списком, кортежей, словарей
"""
import numpy as np
from numpy.testing import assert_equal

import warnings

warnings.filterwarnings("ignore")


def nearest_value(X: np.ndarray, a: float) -> float:
    differences = np.abs(X-a)
    min_difference = np.min(differences)
    nearest_numbers = X[differences == min_difference]
    
    return np.min(nearest_numbers)


X = np.array([[1, 2, 13],
              [15, 6, 8],
              [7, 18, 9]])
a = 7.2

result = nearest_value(X, a)

assert_equal(
    nearest_value(np.array([1, 2, 13]), 10),
    13)
######################################################
assert_equal(
    nearest_value(np.array([-1, 0]), -0.5),
    -1)
######################################################
assert_equal(
    nearest_value(np.array([[[1], [2], [3]], [[4], [5], [6]]]), 4.5),
    4)
######################################################
assert_equal(
    nearest_value(np.array([[1, 2, 13],
                            [15, 6, 8],
                            [7, 18, 9]]), 7.2),
    7)
######################################################
assert_equal(
    nearest_value(np.array([[-1, -2],
                            [-15, -6]]), -100),
    -15)
######################################################
assert_equal(
    nearest_value(np.array([[2, 2],
                            [12, 12]]), 7),
    2)
######################################################
assert_equal(
    nearest_value(np.array([[-2, -2],
                            [-12, -12]]), -7),
    -12)
