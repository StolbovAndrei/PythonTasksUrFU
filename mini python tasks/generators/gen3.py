from datetime import date, timedelta

from gen1 import take


days_of_week = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

@take(6)
def generate_dow(month, day, year):
    current_date = date(year, month, day)
    while True:
        day_index = current_date.weekday()
        yield days_of_week[day_index]
        current_date += timedelta(days=1)

if __name__ == "__main__":
    # for i, day in enumerate(generate_dow(12, 1, 2025)):
    #     print(day)
    #     if i >= 6:
    #         break
    for day in generate_dow(12, 1, 2025):
        print(day)