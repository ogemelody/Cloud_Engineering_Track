# Copy your code from the previous Movies project
def movies_project(movies):
    pass


def main():
    print(
        "Menu:\n0. Exit\n1. List movies\n2. Add movie\n3. Delete movie\n4. Update movie\n5. Stats\n6. Random movie\n7. Search movie\n8. Movies sorted by rating\n9. Movies sorted by year\n10. Filter movies")
    user_choice = int(input("Enter choice (0-10): "))
    if user_choice == 0:
        print("Bye!")
    else:
        print("Press enter to continue")


if __name__ == '__main__':
    main()
