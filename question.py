class Questions:
    def __init__(self, question_text, choices, correct_answer_key):
        self.question_text = question_text
        self.choices = choices
        self.correct_answer_key = correct_answer_key
    def display(self):
        print(f"\nQuestion: {self.question_text}")
        for letter, choice in self.choices.items():
            print(f"{letter}. {choice}")
    def is_correct(self, user_answer_key):
        return user_answer_key.lower() == self.correct_answer_key
    def get_correct_answer_text(self):
        return self.choices.get(self.correct_answer_key, "N/A")