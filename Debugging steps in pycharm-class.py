def count_approved_students(grade_list, grade_cutoff):
    """Count the number of students who are approved based on the grade cutoff."""
    approved_count = 0
    for current_grade in grade_list:
        if current_grade >= grade_cutoff:  # Bug: Should be >= instead of > #Debug: set a break point
            approved_count += 1
    return approved_count


def calculate_average_grade(grade_list):
    """Calculate the average grade."""
    total_sum = sum(grade_list)
    if len(grade_list) <= 0:
        return 0
    return total_sum / len(grade_list)  # Bug: Doesn't handle division by zero if grades is empty


# Debug: select total_sum / len(grade_list) and right click and select evaluate expression and evaluate


def main():
    student_grades = [50, 40, 73, -10, 60]
    # add filter to
    student_grade_filter = [grade for grade in student_grades if grade > 0]
    print(student_grade_filter)
    required_grade = 50  # The grade needed for approval

    print("Analyzing grades...")
    approved_students = count_approved_students(student_grades, required_grade)
    failed_students = len(student_grades) - approved_students
    print(f"Number of approved students: {approved_students}")
    print(f"Number of failed students: {failed_students}")

    print("\nCalculating average grade...")
    average_grade = calculate_average_grade(student_grades)  # Bug: Does not validate grades (e.g., -10 is invalid)
    print(f"Class Average: {average_grade:.2f}")


if __name__ == "__main__":
    main()
