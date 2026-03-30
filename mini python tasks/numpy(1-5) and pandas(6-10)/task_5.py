""" Готов
Реализуйте функцию, которая во входной вещественной матрице X находит все значения nan и заменяет их
на медиану остальных элементов столбца. Если все элементы столбца матрицы nan, то заполняем столбец нулями.

P.S.: в заданиях про numpy прошу не использовать циклы python или их однострочные аналоги для генерации/создания списком, кортежей, словарей
"""

import numpy as np
from numpy.testing import assert_array_equal, assert_array_almost_equal


def replace_nans(X: np.ndarray) -> np.ndarray:
    result = X.copy()
    medians = np.nanmedian(result, axis=0)
    all_nan_cols = np.isnan(medians)
    np.nan_to_num(result, nan=medians, copy=False)
    result[:, all_nan_cols] = 0.0
    
    return result



X = np.array([[np.nan, 4, np.nan], [np.nan, np.nan, 8], [np.nan, 5, np.nan]])
output = replace_nans(X)


######################################################
assert_array_equal(
    replace_nans(np.array([[np.nan], [np.nan], [np.nan]])),
    np.array([[0.0], [0.0], [0.0]]),
)
######################################################
assert_array_equal(replace_nans(np.array([[0, 42, 42]])), np.array([[0, 42, 42]]))
######################################################
assert_array_equal(
    replace_nans(np.array([[np.nan], [1], [np.nan]])), np.array([[1.0], [1.0], [1.0]])
)
######################################################
assert_array_equal(
    replace_nans(np.array([[4], [1], [np.nan]])), np.array([[4], [1], [2.5]])
)
######################################################
assert_array_equal(
    replace_nans(np.array([[-8], [1], [np.nan]])), np.array([[-8], [1], [-3.5]])
)
######################################################
assert_array_almost_equal(
    replace_nans(np.array([[-1.515], [2.252], [np.nan]])),
    np.array([[-1.515], [2.252], [0.3685]]),
)
######################################################
assert_array_equal(
    replace_nans(
        np.array([[np.nan, np.nan, np.nan], [4, np.nan, 5], [np.nan, 8, np.nan]]).T
    ),
    np.array([[0.0, 0.0, 0.0], [4.0, 4.5, 5.0], [8.0, 8.0, 8.0]]).T,
)
