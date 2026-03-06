import datetime
import calendar

today = datetime.datetime.now()
year = today.year
month = today.month

def show_date():
    formatted = today.strftime("\n%d %b %Y\n")
    print(formatted)

def show_calendar():
    print(calendar.month(year, month))
    

def prompt():
    while True:
        print("\nChoose an option:\n")
        print("1. Show today's date")
        print("2. Show today's calendar")
        print("3. Show both\n")
        user_input = input("")

        try:
            choice = int(user_input)
        except ValueError:
            choice = user_input.lower()

        if choice == 1:
            show_date()
        elif choice == 2:
            show_calendar()
        elif choice == 3:
            show_date()
            show_calendar()
        else:
            print(f"\nError: '{choice}' is not a valid choice")


def main():
    prompt()

main()