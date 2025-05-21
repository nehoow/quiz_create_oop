import random
from question import Questions

class QuizGame:
    def __init__(self, filename="quiz.txt"):
        self.filename = filename
        self.questions = []
        self.score = 0