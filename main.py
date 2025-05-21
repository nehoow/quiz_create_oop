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

    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ").strip()

        if choice == '1':
            quiz_creator.create_new_quiz()
        elif choice == '2':
            if quiz_game.load_questions_from_file():
                quiz_game.start_quiz()
            else:
                print("Cannot start quiz. No questions loaded or file not found.")
        elif choice == '3':
            print("Exiting Quiz Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")