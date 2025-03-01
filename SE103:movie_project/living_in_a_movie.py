# Dictionary to store the movies and the rating
import random
import statistics

import matplotlib.pyplot as plt
from colorama import Fore, init

import movie_storage

# Initializes colorama for Windows compatibility
init(autoreset=True)


# Bonus
def plot_rating_histogram(movies):
    """
    Function to create a histogram of movie ratings.
    """
    ratings = list(movies.values())
    ratings = [movie["rating"] for movie in movies.values()]
    plt.figure(figsize=(8, 6))  # Set the figure size
    plt.hist(ratings, bins=10, color='skyblue', edgecolor='black', alpha=0.7)
    plt.title("Distribution of Movie Ratings", fontsize=16)
    plt.xlabel("Ratings", fontsize=12)
    plt.ylabel("Frequency", fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()


# plot_rating_histogram(movies)

def list_movies():
    '''
    The List movies Function
      - Print all the movies in the database,along with their ratings.
    '''
    movies = movie_storage.get_movies()
    each_movie = len(movies)
    print(f"{each_movie} movies in total")

    # Iterate through movies
    for index, (key, value) in enumerate(movies.items()):
        year = value.get('year', 'Unknown Year')  # Default to 'Unknown Year' if missing
        ratings = value.get('ratings', 'No Rating')  # Default to 'No Rating' if missing

        print(f"{index + 1}. {key} ({year}): {ratings}")


def add_movie():
    '''
    Function request for user input of movie name and rating.
    while utilzing the add_movie function from save_movie
    '''
    new_movie_name = input("Enter a movie_name: ")
    new_year = input("Enter Year: ")
    new_rating = float(input("Enter the movie rating(between 1-10: "))
    result = movie_storage.add_movie(new_movie_name, new_year, new_rating)


# delete movie function

def delete_movie():
    """
    delete a movie from the movie database using the function in save_storage.py file
    """
    movie_name_to_delete = input("Enter the name of movie you want to delete: ")
    result = movie_storage.delete_movie(movie_name_to_delete)
    print(result)


# Function to update the movie in the dictionary


def update_movie():
    movies = movie_storage.get_movies()
    user_input = input("Enter a movie name: ")
    updated_rating = float(input("Input new rating of the movie (between 1 -10): "))
    result = movie_storage.update_movie(user_input, updated_rating)
    print(result)


def stats():
    # Extract ratings list
    movies = movie_storage.get_movies()
    ratings = [movie['ratings'] for movie in movies.values()]

    # Average rating
    average = statistics.mean(ratings)
    print(f"Average rating: {average:.1f}")

    # Median rating
    median = statistics.median(ratings)
    print(f"Median rating: {median:.1f}")

    # Best and worst movies
    sorted_movies = sorted(movies.items(), key=lambda item: item[1]['ratings'])
    best_movie = sorted_movies[-1]  # Last item (highest rating)
    worst_movie = sorted_movies[0]  # First item (lowest rating)

    print(f"Best movie: {best_movie[0]}, Rating: {best_movie[1]['ratings']}")
    print(f"Worst movie: {worst_movie[0]}, Rating: {worst_movie[1]['ratings']}")


# random movie
def generate_random_movie():
    movies = movie_storage.get_movies()
    choice_generated_key = random.choice(list(movies.keys()))
    choice_generated_rating = movies[choice_generated_key]
    print(f"Your movie for tonight: {choice_generated_key}, it's rated {choice_generated_rating}")


def search_movie():
    '''
    search all the movies in the database and prints
    all the movies that matched the user’s query, along with the rating.
    '''
    movies = movie_storage.get_movies()
    search_prompt = input("Enter part of movie name: ").lower()  # to make the input uniform using lower()
    movie_match_search_prompt = {}
    for key, value in movies.items():
        if search_prompt in key.lower():
            movie_match_search_prompt[key] = value
    # produces the matching movies based on what was search by user
    if movie_match_search_prompt:
        for key, value in movie_match_search_prompt.items():
            print(f"{key}, {value}")
    else:
        print("Not available")


def movies_sorted_by_rating():
    movies = movie_storage.get_movies()
    # function sorts movie by their ratings in descending order
    sorted_movies = sorted(movies.items(), key=lambda item: item[1]['ratings'], reverse=True)

    for movie, information in sorted_movies:
        print(f"{movie}: Year {information['year']}, Rating {information['ratings']}")


def movies_sorted_by_year():
    movies = movie_storage.get_movies()  # Get the movies dictionary
    user_input = input("Will you want to see the latest movies first or last? first/last: ").lower()

    if user_input == 'first':
        # Sort movies by year in descending order
        sorted_movies = sorted(movies.items(), key=lambda item: int(item[1]['year']), reverse=True)
    else:
        # Sort movies by year in ascending order
        sorted_movies = sorted(movies.items(), key=lambda item: int(item[1]['year']))

    # Loop through sorted movies and print them
    for movie, information in sorted_movies:
        print(f"{movie}: Year {information['year']}, Rating {information['ratings']}")


def filter_movies():
    movies = movie_storage.get_movies()

    # Get user input for filtering criteria, with default values for blank inputs
    minimum_rating = input("Enter the minimum rating of movie (leave blank for no filter): ")
    start_year = input("Enter the start year (leave blank for no filter): ")
    end_year = input("Enter the end year (leave blank for no filter): ")

    # Convert the inputs to appropriate types if they are not empty
    if minimum_rating:
        minimum_rating = float(minimum_rating)
    else:
        minimum_rating = None  # No filter for rating

    if start_year:
        start_year = int(start_year)
    else:
        start_year = None  # No filter for start year

    if end_year:
        end_year = int(end_year)
    else:
        end_year = None  # No filter for end year

    # Filter movies based on the criteria
    for key, details in movies.items():
        movie_year = details["year"]
        movie_rating = details["ratings"]

        # Apply filters
        if (minimum_rating is None or movie_rating >= minimum_rating) and \
                (start_year is None or movie_year >= start_year) and \
                (end_year is None or movie_year <= end_year):
            print(f"{key}, {movie_year}, {movie_rating}")

        # print(f"{key}, {details["year"]}, {details["ratings"]}")


def main():
    # Load movies from storage

    print(Fore.MAGENTA + "********** My Movies Database **********")
    print(
        "Menu:\n0. Exit\n1. List movies\n2. Add movie\n3. Delete movie\n4.\
 Update movie\n5. Stats\n6. Random movie\n7. Search movie\n8. Movies sorted by rating\n9. Movies sorted by year\n10. Filter movies")

    while True:
        choice = input("\nEnter choice (0-10): ")

        # Check if input is numeric and within the valid range
        if not choice.isdigit() or int(choice) > 10:
            print("Invalid input. Please enter a number between 0 and 10.")
            continue  # Ask for input again

        choice = int(choice)  # Convert input to an integer

        if choice == 0:
            print("Bye!")
            break
        elif choice == 1:
            list_movies()
            print(
                "\nMenu:\n0. Exit\n1. List movies\n2. Add movie\n3. Delete movie\n4. Update movie\n5. Stats\n6. Random movie\n7. Search movie\n8. Movies sorted by rating\n9. Movies sorted by year\n10. Filter movies")


        elif choice == 2:
            add_movie()
            print(
                "\nMenu:\n0. Exit\n1. List movies\n2. Add movie\n3. Delete movie\n4. Update movie\n5. Stats\n6. Random movie\n7. Search movie\n8. Movies sorted by rating\n9. Movies sorted by year\n10. Filter movies")

        elif choice == 3:
            delete_movie()
            print(
                "\nMenu:\n0. Exit\n1. List movies\n2. Add movie\n3. Delete movie\n4. Update movie\n5. Stats\n6. Random movie\n7. Search movie\n8. Movies sorted by rating\n9. Movies sorted by year\n10. Filter movies")

        elif choice == 4:
            update_movie()
            print(
                "\nMenu:\n0. Exit\n1. List movies\n2. Add movie\n3. Delete movie\n4. Update movie\n5. Stats\n6. Random movie\n7. Search movie\n8. Movies sorted by rating\n9. Movies sorted by year\n10. Filter movies")

        elif choice == 5:
            stats()
            print(
                "\nMenu:\n0. Exit\n1. List movies\n2. Add movie\n3. Delete movie\n4. Update movie\n5. Stats\n6. Random movie\n7. Search movie\n8. Movies sorted by rating\n9. Movies sorted by year\n10. Filter movies")

        elif choice == 6:
            generate_random_movie()
            print(
                "\nMenu:\n0. Exit\n1. List movies\n2. Add movie\n3. Delete movie\n4. Update movie\n5. Stats\n6. Random movie\n7. Search movie\n8. Movies sorted by rating\n9. Movies sorted by year\n10. Filter movies")

        elif choice == 7:
            search_movie()
            print(
                "\nMenu:\n0. Exit\n1. List movies\n2. Add movie\n3. Delete movie\n4. Update movie\n5. Stats\n6. Random movie\n7. Search movie\n8. Movies sorted by rating\n9. Movies sorted by year\n10. Filter movies")

        elif choice == 8:
            movies_sorted_by_rating()
            print(
                "\nMenu:\n0. Exit\n1. List movies\n2. Add movie\n3. Delete movie\n4. Update movie\n5. Stats\n6. Random movie\n7. Search movie\n8. Movies sorted by rating\n9. Movies sorted by year\n10. Filter movies")

        elif choice == 9:
            movies_sorted_by_year()
            print(
                "\nMenu:\n0. Exit\n1. List movies\n2. Add movie\n3. Delete movie\n4. Update movie\n5. Stats\n6. Random movie\n7. Search movie\n8. Movies sorted by rating\n9. Movies sorted by year\n10. Filter movies")

        elif choice == 10:
            filter_movies()
            print(
                "\nMenu:\n0. Exit\n1. List movies\n2. Add movie\n3. Delete movie\n4. Update movie\n5. Stats\n6. Random movie\n7. Search movie\n8. Movies sorted by rating\n9. Movies sorted by year\n10. Filter movies")


if __name__ == "__main__":
    main()
