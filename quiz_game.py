import random
from question import Questions

GREEN = '\033[92m'
RED = '\033[91m'
BLUE = '\033[94m'
YELLOW = '\033[93m'
RESET = '\033[0m'

class QuizGame:
    def __init__(self, filename="quiz.txt"):
        self.filename = filename
        self.questions = []
        self.score = 0

    def load_questions_from_file(self):
        self.questions = []
        with open(self.filename, "r") as file:
            while True:
                question_line = file.readline().strip()
                if not question_line:
                    break
                question_text = question_line.removeprefix("Question: ")
                choices = {}
                for i in range(4):
                    choice_line = file.readline().strip()
                    letter, answer = choice_line.split(".", 1)
                    choices[letter.strip()] = answer.strip()
                correct_answer_line = file.readline().strip()
                correct_answer_key = correct_answer_line.removeprefix("correct answer: ")
                self.questions.append(Questions(question_text, choices, correct_answer_key))
        if not self.questions:
            return False
        else:
            return True

    def start_quiz(self):
        if not self.questions:
            print("No questions loaded. Please create a quiz first.")
            return
        
        print("\n--- Starting Quiz ---")
        self.score = 0
        quiz_copy = list(self.questions)
        random.shuffle(quiz_copy)

        for i, question_obj in enumerate(quiz_copy):
            print(f"\n{YELLOW}Question {i + 1}:{RESET}")
            question_obj.display()

            while True:
                user_answer_key = input("Your answer (enter the letter): ").strip().lower()
                if user_answer_key in question_obj.choices:
                    break
                else:
                    print("Invalid input. Please enter the letter corresponding to your choice.")

            if question_obj.is_correct(user_answer_key):
                print(f"{GREEN}Correct!{RESET}")
                self.score += 1
            else:
                print(f"{RED}Incorrect.{RESET} The correct answer was {GREEN}{question_obj.get_correct_answer_text()} ({question_obj.correct_answer_key}).{RESET}")

        print(f"\n{GREEN}Quiz finished!{RESET} Your final score is {BLUE}{self.score}/{len(self.questions)}.{RESET}")