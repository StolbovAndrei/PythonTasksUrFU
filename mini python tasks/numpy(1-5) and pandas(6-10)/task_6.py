"""
Вам на вход подается словарь, где ключ - это тип животного, а значение - словарь с
признаками этого животного, где ключ - тип признака,
а значение - значение признака (Типичный json проще говоря).
Наименования признаков животного - всегда строки. Значения признаков - любой из типов pandas.

Вам следует создать табличку, где по строчкам будут идти животные, а по колонкам - их признаки
* Тип животного нужно выделить в отдельную колонку Type
* Строки отсортированы по типу животного в алфавитном порядке
* Колонки отсортированы в алфавитном порядке, кроме колонки Type - она первая
* Индексы строк - ряд натуральных чисел начиная с 0 без пропусков
Имейте в виду, что признаки у двух животных могут не совпадать,
значит незаполненные данные нужно заполнить Nan значением.

Верните на выходе табличку(DataFrame), в которой отсутствуют Nan значения.
При этом могут отсутствовать некоторые признаки, но животные должны присутствовать все.
Изначальные типы значений из словаря: int64, float64, bool и.т.д.
должны сохраниться и в конечной табличке, а не превратиться в object-ы.
(От удаляемых признаков этого, очевидно, не требуется).

"""

import numpy as np
import pandas as pd
from pandas._testing import assert_frame_equal


def ZOOtable(zoo: dict) -> pd.DataFrame:
    if not zoo:
        return pd.DataFrame({'Type': []})
    
    sorted_animals = sorted(zoo.keys())
    
    df = pd.DataFrame({'Type': sorted_animals})
    
    all_features = set()
    for animal_features in zoo.values():
        all_features.update(animal_features.keys())

    for feature in sorted(all_features):
        values = [zoo[animal].get(feature, np.nan) for animal in sorted_animals]
        df[feature] = values
    
    cols_to_keep = ['Type']
    for col in df.columns:
        if col != 'Type' and df[col].notna().all():
            cols_to_keep.append(col)
    
    return df[cols_to_keep]


######################################################
ZOO = {
    "cat": {"color": "black", "tail_len": 50.0, "injured": False},
    "dog": {"age": 6, "tail_len": 30.5, "injured": True},
}

df = ZOOtable(ZOO)
print(df)
assert_frame_equal(
    df.reset_index(drop=True),
    pd.DataFrame(
        {"Type": ["cat", "dog"], "injured": [False, True], "tail_len": [50.0, 30.5]}
    ),
)
######################################################
ZOO = {"cat": {"color": "black"}, "dog": {"age": 6}}

df = ZOOtable(ZOO)

assert_frame_equal(df.reset_index(drop=True), pd.DataFrame({"Type": ["cat", "dog"]}))
######################################################
