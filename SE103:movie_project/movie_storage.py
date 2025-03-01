import json


def get_movies():
    """
    Returns a dictionary of dictionaries that
    contains the movies information in the database.

    The function loads the information from the JSON
    file and returns the data.
    """

    try:
        with open("data.json", "r") as file:
            return json.load(file)  # Load movies from JSON
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading movies: {e}")
        return {}  # Return an empty dictionary if the file is missing


# print(get_movies())
def save_movies(movies):
    """
    Gets all your movies as an argument and saves them to the JSON file.
    """
    try:
        with open("data.json", "w") as file:
            json.dump(movies, file, indent=4)
    except Exception as e:
        print(f"Error saving movie: {e}")


def add_movie(title, year, rating):
    """
    Adds a movie to the movies database.
    Loads the information from the JSON file, adds the movie,
    and saves it.
    """
    movies = get_movies()

    while True:
        if not title:  # Check if title is empty
            print("Title cannot be empty.")
            title = input("Enter title of Movie: ").strip()
            # continue

        if not (year.isdigit() and len(year) == 4):  # Check if year is a 4-digit number
            print("Invalid year input. Please enter a valid 4-digit year.")
            year = input("Enter year of movie (4-digit year): ").strip()
            continue
        year = int(year)  # Convert to integer after validation

        try:
            rating = float(rating)  # Convert rating to float
            if not (1 <= rating <= 10):  # Ensure rating is between 1 and 10
                print("Invalid rating input. Rating should be between 1 and 10.")  #
                rating = input("Enter movie rating (1 to 10): ").strip()
                # continue
        except ValueError:
            print("Invalid rating input. Please enter a number (e.g., 8.5).")
            # continue

        break  # Exit loop only when all inputs are valid

    movies[title] = {
        "year": year, "ratings": rating
    }
    try:
        save_movies(movies)
        print(f"Movie '{title}' added successfully!")
    except Exception as e:
        print(f"Error saving movie: {e}")


# add_movie()

def delete_movie(title):
    """
    Deletes a movie from the movies database.
    Loads the information from the JSON file, deletes the movie,
    and saves it. The function doesn't need to validate the input.
    """

    movies = get_movies()
    if title in movies:
        del movies[title]
        save_movies(movies)
        return f"Movie '{title}' deleted successfully!"
    else:
        return f"Movie '{title}' not found in file"


# delete_movie()
def update_movie(title, new_rating):
    """
    Updates a movie from the movies database.
    Loads the information from the JSON file, updates the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = get_movies()
    if title in movies:
        existing_year = movies[title]['year']  # Preserve the existing year

        if 1 <= new_rating <= 10:
            movies[title]['ratings'] = new_rating  # Only update the rating
            save_movies(movies)
            # return "Movies after save:", get_movies()
            return f"Updated '{title}': Year {existing_year}, New Rating {new_rating}"  # Print confirmation
        else:
            return "Invalid rating. Please enter a value between 1 and 10."  # Fix incorrect message

    else:
        return f"Movie '{title}' doesn't exist!"