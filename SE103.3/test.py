if message == "help":
    user_command = input(
        "Available commands: \nhelp\nshow_countries\ntop_countries <num_countries>\nships_by_types\nsearch_ship\nspeed_histogram")

        elif user_command == "show_countries":
                print(show_countries())
                break

            elif user_command.startswith("top_countries"):
                parts = user_command.split()
                if len(parts) == 2:
                    try:
                        num_countries = int(parts[1])  # Get the number
                        countries = show_countries()  # Get the list of countries
                        top_countries(num_countries, countries)  # Call the function
                        break
                    except ValueError:
                        print("Please enter a valid number.")
                else:
                    print("Please provide the number of countries.")
    else:
        print("Unknown Command")








-----------------------


def main():
    message_input = input("Welcome to the Ships CLI! Enter 'help' to view available commands.\n" ).lower()
    if message_input == "help":
        print("Available commands: \nhelp\nshow_countries\ntop_countries <num_countries> \n")
    while True:
        #user_command = input("Available commands: \nhelp\nshow_countries\ntop_countries <num_countries> \n")
        user_command = input(" ")
        if user_command == "help":
            print("Available commands: \nhelp\nshow_countries\ntop_countries <num_countries>: \n")

        if user_command == "show_countries":
            show_countries()

        elif user_command.startswith("top_countries"):
            parts = user_command.split()
            if len(parts) == 2:
                try:
                    num_countries = int(parts[1])  # Get the number
                    countries = show_countries()  # Get the list of countries
                    top_countries(num_countries, countries)  # Call the function
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("Please provide the number of countries.")
        else:
            print("Unknown Command")


if __name__ == '__main__':
    main()


