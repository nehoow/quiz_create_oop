import os
from question import Questions

class QuizCreator:
    def __init__(self, filename="quiz.txt"):
        self.filename = filename