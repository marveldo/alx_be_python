from datetime import datetime , timedelta

def display_current_datetime():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f'{current_date}')

def calculate_future_date():
    days_amount = float(input('Enter the number of days to add to the current date: '))
    future_date = datetime.now() + timedelta(days=days_amount)
    print(f'{future_date.strftime("%Y-%m-%d")}')
if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
