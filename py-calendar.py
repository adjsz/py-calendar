import datetime
import calendar

today = datetime.datetime.now()
current_year = today.year
current_month = today.month

def show_date():
    formatted = today.strftime("\n%d %b %Y\n")
    print(formatted)

def show_calendar():
    print(calendar.month(current_year, current_month))

def generate_calendar():
    set_year = input("\nSet a year: ")
    set_month = input("\nSet a month (1-12): ")

    try:
        set_year = int(set_year)
        set_month = int(set_month)
    except ValueError:
          print("\nError: Please type numbers only.\n")
          return

    if set_month < 1 or set_month > 12:
        print("\nError: Month can only be between 1 and 12.")
        return

    print("\n", calendar.month(set_year, set_month))

def prompt():
    while True:
        print("\nOptions:\n")
        print("1. Show today's date")
        print("2. Show today's calendar")
        print("3. Generate calendar")
        print("4. Show both")
        print("5. Exit\n")
        user_input = input("Enter your choice: ")
        
        try:
                choice = int(user_input)
        except ValueError:
                print("\nError: invalid choice")
                continue

        if choice == 1:
                show_date()
        elif choice == 2:
                show_calendar()
        elif choice == 3:
                generate_calendar()
        elif choice == 4:
                show_date()
                show_calendar()
        elif choice == 5:
                break # exits
        else:
                print("\nError: invalid choice")
                continue


def main():
    prompt()

main()