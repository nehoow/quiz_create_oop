import random
from question import Questions

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