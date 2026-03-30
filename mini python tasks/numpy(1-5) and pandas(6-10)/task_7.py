"""
Необходимо вернуть исходную таблицу с добавленным в конце столбцом полных лет жизни.

"""

import pandas as pd
from dateutil.relativedelta import relativedelta
from pandas._testing import assert_frame_equal
import re
from datetime import datetime

def rus_feature(df: pd.DataFrame) -> pd.DataFrame:
    def parse_date(date_str):
        match = re.match(r'(\d+) ([^\s]+) (\d+) г\.', date_str)
        if not match:
            raise ValueError(f"Неверный формат даты: {date_str}")
        
        day = int(match.group(1))
        month_name = match.group(2)
        year = int(match.group(3))
        
        months = {
            'января': 1, 'февраля': 2, 'марта': 3, 'апреля': 4,
            'мая': 5, 'июня': 6, 'июля': 7, 'августа': 8,
            'сентября': 9, 'октября': 10, 'ноября': 11, 'декабря': 12
        }
        
        month = months.get(month_name)
        if month is None:
            raise ValueError(f"Неизвестный месяц: {month_name}")     
        return datetime(year, month, day)
    
    df['birth_date'] = df['Дата рождения'].apply(parse_date)
    df['death_date'] = df['Дата смерти'].apply(parse_date)
    
    df['Полных лет'] = df.apply(
        lambda row: relativedelta(row['death_date'], row['birth_date']).years, 
        axis=1
    )
    
    return df[['Имя', 'Дата рождения', 'Дата смерти', 'Полных лет']]



names = pd.DataFrame(
    {
        "Имя": ["Никола Тесла", "Альберт Эйнштейн"],
        "Дата рождения": ["10 июля 1856 г.", "14 марта 1879 г."],
        "Дата смерти": ["7 января 1943 г.", "18 апреля 1955 г."],
    }
)

assert_frame_equal(
    rus_feature(names),
    pd.DataFrame(
        {
            "Имя": ["Никола Тесла", "Альберт Эйнштейн"],
            "Дата рождения": ["10 июля 1856 г.", "14 марта 1879 г."],
            "Дата смерти": ["7 января 1943 г.", "18 апреля 1955 г."],
            "Полных лет": [86, 76],
        }
    ),
)

names = pd.DataFrame(
    {
        "Имя": ["Никола Тесла"],
        "Дата рождения": ["10 июля 1856 г."],
        "Дата смерти": ["7 января 1857 г."],
    }
)

assert_frame_equal(
    rus_feature(names),
    pd.DataFrame(
        {
            "Имя": ["Никола Тесла"],
            "Дата рождения": ["10 июля 1856 г."],
            "Дата смерти": ["7 января 1857 г."],
            "Полных лет": [0],
        }
    ),
)

names = pd.DataFrame(
    {
        "Имя": ["Никола Тесла"],
        "Дата рождения": ["1 января 2000 г."],
        "Дата смерти": ["31 декабря 2000 г."],
    }
)
assert_frame_equal(
    rus_feature(names),
    pd.DataFrame(
        {
            "Имя": ["Никола Тесла"],
            "Дата рождения": ["1 января 2000 г."],
            "Дата смерти": ["31 декабря 2000 г."],
            "Полных лет": [0],
        }
    ),
)

names = pd.DataFrame(
    {
        "Имя": ["Никола Тесла"],
        "Дата рождения": ["1 января 2000 г."],
        "Дата смерти": ["1 января 2001 г."],
    }
)

assert_frame_equal(
    rus_feature(names),
    pd.DataFrame(
        {
            "Имя": ["Никола Тесла"],
            "Дата рождения": ["1 января 2000 г."],
            "Дата смерти": ["1 января 2001 г."],
            "Полных лет": [1],
        }
    ),
)
