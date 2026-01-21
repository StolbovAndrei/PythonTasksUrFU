from datetime import date

from gen2 import business_days
from gen3 import generate_dow


def business_plus_generate():
    business = business_days(today, deadline)
    generate = generate_dow(today.month, today.day, today.year)

    while True:
        try:
            yield(next(business), next(generate))
        except StopIteration:
            break

if __name__ == "__main__":
    today = date.today()
    print("Enter deadline YYYY/MM/DD:")
    deadline = date(int(input("year: ")), int(input("month: ")), int(input("day: ")))

    for info in business_plus_generate():
        print(info)