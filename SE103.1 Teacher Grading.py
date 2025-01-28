def get_grade(subject):
    """
    function get the grade of each subject
    """
    try:
        while True:
            if subject == "English":
                english_grade = float(input("Enter English grade:"))
                return english_grade
            elif subject == "Math":
                math_grade = float(input("Enter Math grade: "))
                return math_grade  # Solved: maybe I might need a if that handles input based on subject, let's see
            break
    except ValueError:
        print("Expected a number")


def get_student_info():
    """
    function collects the students informations
    (name, English and Math grade) and store the
    information in a dictionary
    """
    student_name = input("Enter student name: ")
    english_grade = get_grade("English")
    math_grade = get_grade("Math")
    student_information_dictionary = {}
    student_information_dictionary["Name"] = student_name
    student_information_dictionary["English"] = english_grade
    student_information_dictionary["Math"] = math_grade
    return student_information_dictionary


def print_student_info(students):
    """
    function that will print information about the students.
  it used the dictionary comprrehension and generator expression
  like next, max. To get the best grade and average grade
    """
    # students = collection_of_students_information
    print(students)
    for student in students:
        best_grade_key = max((key for key in student if key != 'Name'), key=student.get)
        best_grade = student[best_grade_key]
        english_grade_key = next((key for key in student if key == 'English'), None)
        print(english_grade_key)
        english_grade = student[english_grade_key]
        math_grade_key = next((key for key in student if key == 'Math'))
        math_grade = student[math_grade_key]
        average_grade = (math_grade + english_grade) / 2
        print(f"Student: {student['Name']}, Best Grade: {best_grade}, Average Grade: {average_grade} ")


def calculate_average_grades(students):
    """
    :param students: gets the information
    :return: the average grade per subject( English,Math) and overall average grade across all subject
    """
    english = []
    math = []
    for student in students:
        english.append(student["English"])
        math.append(student["Math"])
    average_grades_per_subject_english = sum(english) / len(english)
    average_grades_per_subject_math = sum(math) / len(math)
    overall_average_grade_across_all_subjects = (
                                                            average_grades_per_subject_english + average_grades_per_subject_math) / 2
    return average_grades_per_subject_english, average_grades_per_subject_math, overall_average_grade_across_all_subjects


def calculate_failing_grades(students):
    GRADE = 55
    failing_students = []
    for student in students:
        name = student["Name"]
        failed_subjects = 0
        if student["English"] < GRADE:
            failed_subjects += 1
        if student["Math"] < GRADE:
            failed_subjects += 1
        failing_students.append((name, failed_subjects))
    return failing_students


def main():
    collection_of_students_information = []
    number_of_students = int(input("Enter the number of students: "))
    # english_grade = get_grade("Math")
    # print(english_grade)

    # collect information for each student and appends into the list
    for i in range(number_of_students):
        collection_of_students_information.append(get_student_info())

    # print(collection_of_students_information)
    # print_student_info(collection_of_students_information)
    calculate_average_grades(collection_of_students_information)
    # print_student_info(students)
    average_grades_per_subject_english, average_grades_per_subject_math, overall_average_grade_across_all_subjects = calculate_average_grades(
        collection_of_students_information)
    print("\nAverage grades per subject:")
    print(f"English: {average_grades_per_subject_english}\nMath:{average_grades_per_subject_math}")

    print(f"\nOverall average grade across all subjects: {overall_average_grade_across_all_subjects:.2f}")
    failing_results = calculate_failing_grades(collection_of_students_information)
    #name, failed_subjects = calculate_failing_grades(collection_of_students_information)
    for name, failed_subjects in failing_results:
        print(f"{name}: {failed_subjects} failing grade(s)")


if __name__ == '__main__':
    main()
