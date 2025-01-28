# Dictionary to store the movies and the rating
import random
import statistics

def list_movies(movies):
    '''
    The List movies Function
      - Print all the movies in the database,along with their rating.
    '''
    each_movie = len(movies)
    print(f"{each_movie} movies in total")
    for each_movie, (key, value) in enumerate(movies.items()):
        each_movie += 1
        print(f"{key}: {value}")


def add_movie(movies):
    '''
    Function request for user input of movie name and rating.
    '''
    new_movie_name = input("Enter a movie_name: ")
    while True:
        try:
            new_rating = float(input("Enter the movie rating(between 1 -10: "))
            if 1 <= new_rating <= 10:
                break
            else:
                print("Please enter a rating between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 10.")

    #check movie before adding it to the list
    if new_movie_name in movies:
        print(f"The movie {new_movie_name} already exist")

    else:
        movies[new_movie_name] = new_rating
        print(f"Movie '{new_movie_name}' added/updated with a rating of {new_rating}.")
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
        updated_rating = float(input("input new rating of the movie (between 1 -10: "))
        movies[user_input] = updated_rating
    else:
        print(f"Movie {user_input} doesn't exist!")
    print(movies)



def stats(movies):
    # function display the Average, Median,best, and worst movie
    average = statistics.mean(movies.values())
    print(f"Average rating: {average:.2f}")

    #median rating
    median = statistics.median(movies.values())
    print(f"Median rating: {median:.2f}")

    # best and worst  movie
    sorted_by_values = dict(sorted(movies.items(), key=lambda item: item[1]))
    best_movie = list(sorted_by_values.items())[-1]
    worst_movie = list(sorted_by_values.items())[0]
    print(f"Best movie: {best_movie[0]}, {best_movie[1]} ")
    print(f"Worst movie: {worst_movie[0]}, {worst_movie[1]} ")

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
    sorted_movies = sorted(movies.items(), key=lambda item: item[1], reverse=True)

    for movie in sorted_movies:
        print(f"{movie[0]}, {movie[1]}")


def main():
    movies = {
        "The Shawshank Redemption": 9.5,
        "Pulp Fiction": 8.8,
        "The Room": 3.6,
        "The Godfather": 9.2,
        "The Godfather: Part II": 9.0,
        "The Dark Knight": 9.0,
        "12 Angry Men": 8.9,
        "Everything Everywhere All At Once": 8.9,
        "Forrest Gump": 8.8,
        "Star Wars: Episode V": 8.7
    }

    print("********** My Movies Database **********")
    while True:
        print("\nMenu: ")
        print("1. List movies")
        print("2. Add Movie")
        print("3. Delete Movie")
        print("4. Update Movie")
        print("5. Stats")
        print("6. Random Movie")
        print("7. Search Movie")
        print("8. Movies sorted by rating")

        choice = input("\nEnter choice (1-8): ")

        if choice == "1":
            list_movies(movies)
        elif choice == "2":
            add_movie(movies)
        elif choice == "3":
            delete_movie(movies)
        elif choice == "4":
            update_movie(movies)
        elif choice == "5":
            stats(movies)
        elif choice == "6":
            generate_random_movie(movies)
        elif choice == "7":
            search_movie(movies)
        elif choice == "8":
            movies_sorted_by_rating(movies)
            break
        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()
