# Dictionary to store the movies and the rating
import random
import statistics
import matplotlib.pyplot as plt
from colorama import Fore, Style, init

# Initializes colorama for Windows compatibility
init(autoreset=True)


# Bonus
def plot_rating_histogram(movies):
    """
    Function to create a histogram of movie ratings.
    """
    ratings = list(movies.values())
    plt.figure(figsize=(8, 6))  # Set the figure size
    plt.hist(ratings, bins=10, color='skyblue', edgecolor='black', alpha=0.7)
    plt.title("Distribution of Movie Ratings", fontsize=16)
    plt.xlabel("Ratings", fontsize=12)
    plt.ylabel("Frequency", fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()


def list_movies(movies):
    '''
    The List movies Function
      - Print all the movies in the database,along with their rating.
    '''
    each_movie = len(movies)
    print(f"{each_movie} movies in total")
    for each_movie, (key, value) in enumerate(movies.items()):
        each_movie += 1
        print(f"{key} ({value["year"]}): {value["ratings"]}")


def add_movie(movies):
    '''
    Function request for user input of movie name and rating.
    '''
    new_movie_name = input("Enter a movie_name: ")
    while True:
        try:
            new_rating = float(input("Enter the movie rating(between 1 -10: "))
            new_year = input("Enter Year: ")
            if 1 <= new_rating <= 10 and new_year.isdigit():
                break
            else:
                print("Please enter a rating between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 10.")

    # check movie before adding it to the list
    if new_movie_name in movies:
        print(f"The movie {new_movie_name} already exist")

    else:
        movies[new_movie_name] = {'year': new_year, 'ratings': new_rating }
        print(f"Movie '{new_movie_name}' added with a rating of {new_rating} and year {new_year}.")
        return movies


# delete movie function
def delete_movie(movies):
    movie_name_to_delete = input("Enter the name of movie you want to delete: ")
    if movie_name_to_delete in movies:
        del movies[movie_name_to_delete]
        print(f"Movie {movie_name_to_delete} successfully deleted")
    else:
        print("Movie does not exist in Dictionary")


# Function to update the movie in the dictionary
def update_movie(movies):
    user_input = input("Enter a movie name: ")

    if user_input in movies:
        existing_year = movies[user_input]['year']  # Preserve the existing year
        updated_rating = float(input("Input new rating of the movie (between 1 -10): "))

        if 1 <= updated_rating <= 10:
            movies[user_input]['ratings'] = updated_rating  # Only update the rating
            print(f"Updated '{user_input}': Year {existing_year}, New Rating {updated_rating}")  #  Print confirmation
        else:
            print("Invalid rating. Please enter a value between 1 and 10.")  # Fix incorrect message

    else:
        print(f"Movie '{user_input}' doesn't exist!")  #  Correct error message

    return movies  #  Always return the updated dictionary


def stats(movies):
    # Extract ratings list
    ratings = [movie['ratings'] for movie in movies.values()]

    # Average rating
    average = statistics.mean(ratings)
    print(f"Average rating: {average:.2f}")

    # Median rating
    median = statistics.median(ratings)
    print(f"Median rating: {median:.2f}")

    # Best and worst movies
    sorted_movies = sorted(movies.items(), key=lambda item: item[1]['ratings'])
    best_movie = sorted_movies[-1]  # Last item (highest rating)
    worst_movie = sorted_movies[0]  # First item (lowest rating)

    print(f"Best movie: {best_movie[0]}, Rating: {best_movie[1]['ratings']}")
    print(f"Worst movie: {worst_movie[0]}, Rating: {worst_movie[1]['ratings']}")


# random movie
def generate_random_movie(movies):
    choice_generated_key = random.choice(list(movies.keys()))
    choice_generated_rating = movies[choice_generated_key]
    print(f"Your movie for tonight: {choice_generated_key}, it's rated {choice_generated_rating}")


def search_movie(movies):
    '''search all the movies in the database and prints
    all the movies that matched the user’s query, along with the rating.'''
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


def movies_sorted_by_rating(movies):
    # function sorts movie by their ratings in descending order
    sorted_movies = sorted(movies.items(), key=lambda item: item[1]['ratings'], reverse=True)

    for movie, information in sorted_movies:
        print(f"{movie}: Year {information['year']}, Rating {information['ratings']}")



def main():
    movies = {
        "The Shawshank Redemption": {'year': 2023, 'ratings':9.5},
        "Pulp Fiction": {'year': 1923, 'ratings': 8.8},
        "The Room": {'year': 1323, 'ratings':3.6},
        "The Godfather": {'year': 1823, 'ratings':9.2},
        "The Godfather: Part II": {'year': 2021, 'ratings':9.0},
        "The Dark Knight": {'year': 2022, 'ratings':9.0},
        "12 Angry Men": {'year': 2020, 'ratings':8.9},
        "Everything Everywhere All At Once": {'year': 1576, 'ratings':8.9},
        "Forrest Gump": {'year': 1807, 'ratings':8.8},
        "Star Wars: Episode V": {'year': 2024, 'ratings':8.7}
    }
    # plot_rating_histogram(movies)

    print(Fore.MAGENTA + "********** My Movies Database **********")
    print("Menu:\n0. Exit\n1. List movies\n2. Add movie\n3. Delete movie\n4. Update movie\n5. Stats\n6. Random movie\n7. Search movie\n8. Movies sorted by rating\n9. Movies sorted by year\n10. Filter movies")

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
            list_movies(movies)
        elif choice == 2:
            add_movie(movies)
        elif choice == 3:
            delete_movie(movies)
        elif choice == 4:
            update_movie(movies)
        elif choice == 5:
            stats(movies)
        elif choice == 6:
            generate_random_movie(movies)
        elif choice == 7:
            search_movie(movies)
        elif choice == 8:
            movies_sorted_by_rating(movies)
        elif choice == 9:
            movies_sorted_by_year(movies)
        elif choice == 10:
            filter_movies(movies)


if __name__ == "__main__":
    main()
