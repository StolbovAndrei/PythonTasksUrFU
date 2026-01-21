"""
Верните максимальное значение, минимальное значение, медиану, среднее,
дисперсию возраста погибших мужчин. Именно в данном порядке.
"""
import pandas as pd


def men_stat(df: pd.DataFrame) -> tuple[float, float, float, float, float]:

    men = df[(df['Sex'] == 'male') & (df['Survived'] == 0)]
    age = men['Age'].dropna()
    
    max_age = age.max()
    min_age = age.min()
    median_age = age.median()
    mean_age = age.mean()
    var_age = age.var()
    
    return max_age, min_age, median_age, mean_age, var_age


df = pd.read_csv('titanic_train.csv', index_col='PassengerId')
output = men_stat(df)
print(output)
