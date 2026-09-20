from quiz import Quiz


def main():
    """Run the Quiz / Exam Management System."""

    quiz = Quiz("questions.json")

    while True:
        print("\n===================================")
        print("     QUIZ / EXAM MANAGEMENT")
        print("===================================")
        print("1. Start Quiz")
        print("2. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            student_name = input("Enter student name: ").strip()

            if not student_name:
                print("Student name cannot be empty.")
                continue

            quiz.load_questions()
            score = quiz.start_quiz()

            if score is not None:
                quiz.save_result(student_name)

        elif choice == "2":
            print("Thank you for using the system.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()