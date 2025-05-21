from quiz_create import QuizCreator
from quiz_game import QuizGame

def display_menu():
    """Displays the main menu options to the user."""
    print("\n--- Quiz Application Menu ---")
    print("1. Create New Quiz")
    print("2. Take Quiz")
    print("3. Exit")
    print("----------------------------")

def main():
    quiz_filename = "quiz.txt"
    quiz_creator = QuizCreator(quiz_filename)
    quiz_game = QuizGame(quiz_filename)