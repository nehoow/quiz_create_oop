import os
from question import Questions

class QuizCreator:
    def __init__(self, filename="quiz.txt"):
        self.filename = filename
    def create_quiz_item(self):
        question_input = input("Enter your question or type 'exit' to finish: ")
        if question_input.lower() == "exit":
            return None

        answers = {}
        answers['a'] = input("Enter answer a: ")
        answers['b'] = input("Enter answer b: ")
        answers['c'] = input("Enter answer c: ")
        answers['d'] = input("Enter answer d: ")

        correct_answer_key = input("Enter the correct answer using (a,b,c, or d): ").lower()
        while correct_answer_key not in answers:
            print("Invalid input! Enter the correct answer (a,b,c, or d)")
            correct_answer_key = input("Enter the correct answer using (a,b,c, or d): ").lower()

        return Questions(question_input, answers, correct_answer_key)
    def write_quiz_to_file(self, question_obj):
        with open(self.filename, "a") as file:
            file.write(question_obj.to_file_format())