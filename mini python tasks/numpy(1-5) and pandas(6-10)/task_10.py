"""
Выведите список имен незамужних женщин(Miss) отсортированный по популярности.

В полном имени девушек имя - это первое слово без скобок после Miss.
Остальные строки не рассматриваем.
Девушки с одинаковой популярностью сортируются по имени в алфавитном порядке.
Слово/имя - подстрока без пробелов. Популярность - количество таких имен в таблице.
"""

import pandas as pd
import warnings
import re

warnings.filterwarnings("ignore")


def fename_stat(df: pd.DataFrame) -> pd.DataFrame:

    miss_women = df[df['Name'].str.contains('Miss', na=False) & 
                    df['Name'].notna() & 
                    (df['Name'].str.len() > 0)]

    def extract_first_name(name):

        name = re.sub(r'\([^)]*\)', '', name)

        match = re.search(r'Miss[ .]*([A-Za-z]+)', name)
        return match.group(1) if match else None
    
    miss_women['Имя'] = miss_women['Name'].apply(extract_first_name)
    
    valid_names = miss_women[miss_women['Имя'].notna()]
    name_counts = valid_names['Имя'].value_counts().reset_index()
    name_counts.columns = ['Имя', 'Популярность']
    
    result = name_counts.sort_values(['Популярность', 'Имя'], ascending=[False, True])
    
    return result[['Имя', 'Популярность']]


df = pd.read_csv("titanic_train.csv", index_col="PassengerId")
output = fename_stat(df)
print(output)