from collections import Counter

from load_data import load_data

all_data = load_data()


def show_countries():
    """
    this function shows all the countries value in the
    ships_data json file without duplicates
    :return: list of countries
    """

    countries = set()  # using set as it does not accept duplicates
    # Iterate over each ship in the data
    for ship in all_data['data']:
        if 'COUNTRY' in ship:  # Check if the country is already in the list
            countries.add(ship['COUNTRY'])
    return sorted(countries)


def top_countries(num_countries):
    """

    :param num_countries: get the number of top_countries user want to retrieve
    :return: it list the top countries and the total count
    """
    country_counter = Counter()
    for ship in all_data['data']:
        if 'COUNTRY' in ship:  # Ensure the key exists
            country_counter[ship['COUNTRY']] += 1
    top_list = country_counter.most_common(num_countries)
    for country, count in top_list:
        print(f"{country}: {count}")


def main():
    """
    :return: call the show_countries and top_countries
    """

    message_input = input("Welcome to the Ships CLI! Enter \
'help' to view available commands.\n").lower()
    if message_input == "help":
        print("Available commands: \nhelp\nshow_countries\ntop_countries <num_countries>\n")
    while True:
        user_command = input(" ")
        if user_command == "help":
            print("Available commands: \nhelp\nshow_countries\ntop_countries <num_countries>:\n")

        elif user_command == "show_countries":
            countries = show_countries()
            for country in countries:
                print(country)

        elif user_command.startswith("top_countries"):
            parts = user_command.split()
            if len(parts) == 2:
                try:
                    num_countries = int(parts[1])  # Get the number
                    top_countries(num_countries)  # Call the function
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("Please provide the number of countries.")
        else:
            print("Unknown Command")


if __name__ == '__main__':
    main()
