from datetime import timedelta, date


def business_days(start_date, end_date):
    current_date = start_date
    while current_date <= end_date:
        if current_date.weekday() < 5:
            yield current_date
        current_date += timedelta(days=1)

if __name__ == "__main__":
    print("Enter deadline YYYY/MM/DD:")
    deadline = date(int(input("year: ")), int(input("month: ")), int(input("day: ")))
    today = date.today()

    workdays_list = list(business_days(today, deadline))
    print(f"number of working days: {len(workdays_list)}")