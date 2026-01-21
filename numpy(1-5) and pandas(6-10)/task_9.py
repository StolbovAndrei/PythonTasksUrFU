"""
Сделать сводную таблицу по максимальному возрасту для пола и класса.
"""
import pandas as pd


def age_stat(df: pd.DataFrame) -> pd.DataFrame:
    result = df.pivot_table(
        values='Age', 
        index='Sex', 
        columns='Pclass', 
        aggfunc='max'
    )
    return result


df = pd.read_csv('titanic_train.csv', index_col='PassengerId')
output = age_stat(df)
print(output)
