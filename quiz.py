import json
import random


class Quiz:
    """Manage quiz questions and calculate the final score."""

    def __init__(self, question_file):
        self.question_file = question_file
        self.questions = []
        self.score = 0

    def load_questions(self):
        """Load questions from a JSON file."""
        try:
            with open(self.question_file, "r", encoding="utf-8") as file:
                self.questions = json.load(file)

        except FileNotFoundError:
            print("Question file not found.")
            self.questions = []

        except json.JSONDecodeError:
            print("Invalid question file format.")
            self.questions = []

    def start_quiz(self):
        """Start the quiz and collect answers."""
        if not self.questions:
            print("No questions available.")
            return

        random.shuffle(self.questions)
        self.score = 0

        print("\n========== QUIZ STARTED ==========\n")

        for number, question in enumerate(self.questions, start=1):

            print(f"{number}. {question['question']}")

            for index, option in enumerate(question["options"], start=1):
                print(f"{index}. {option}")

            while True:
                try:
                    choice = int(input("Enter your answer: "))

                    if 1 <= choice <= len(question["options"]):
                        break

                    print("Please select a valid option.")

                except ValueError:
                    print("Please enter a number.")

            selected_answer = question["options"][choice - 1]

            if selected_answer.lower() == question["answer"].lower():
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! Correct answer: {question['answer']}\n")

        print("========== QUIZ FINISHED ==========")
        print(f"Your Score: {self.score}/{len(self.questions)}")

        return self.score

    def save_result(self, student_name):
        """Save quiz result to JSON file."""
        result = {
            "student_name": student_name,
            "score": self.score,
            "total_questions": len(self.questions)
        }

        try:
            try:
                with open("results.json", "r", encoding="utf-8") as file:
                    results = json.load(file)
            except (FileNotFoundError, json.JSONDecodeError):
                results = []

            results.append(result)

            with open("results.json", "w", encoding="utf-8") as file:
                json.dump(results, file, indent=4)

            print("Result saved successfully.")

        except OSError as error:
            print(f"Error saving result: {error}")