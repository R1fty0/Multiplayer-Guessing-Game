class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def get_score(self):
        """ Returns the player's current score. """
        return self.score

    def set_score(self, num_of_points):
        """ Adds the given amount of points to the player's score."""
        try:
            self.score = num_of_points
        except ValueError:
            print("Error: Score is not an integer value.")


class SceneManagement:
    def __init__(self, game_name: str, menu_name: str, scoreboard_name: str):
        """ Handles the execution of each scene in the game. """
        self.game = game_name   # the name of the game scene
        self.menu = menu_name   # the name of the menu scene
        self.scoreboard = scoreboard_name   # the name of the scoreboard scene
        self.current_scene = menu_name  # the current scene active in the game. menu is set active by default.

    def get_current_scene(self):
        """ Gets the current scene that is running in the game. """
        return self.current_scene

    def set_current_scene(self, next_scene):
        """ Sets the current scene of the game. """
        self.current_scene = next_scene

    def quit_game(self):
        """ Quits the game"""
        import sys
        sys.exit()


class Game:
    def print_question(self, question):
        """ Shows the user the question. """
        print(f"Here is your question: {question}")

    def lock_answer(self):
        """ Asks the user to input their answer, and locks it in. """
        user_answer = input("What is your answer?: ")
        try:
            if type(user_answer) == type(int):
                # Send answer to server for verification.
                pass
        except ValueError:
            print("You have not entered a number for your answer! Please try again.")
            self.lock_answer()


    def ask_for_hint(self, hint):
        """ Asks the user if they want a hint, and provides them one if they so choose."""
        choice = input("Would you like a hint?: Press (1) for Yes and any other key for No.")
        try:
            if int(choice) == 1:
                print(f"You have chosen to view a hint! \nHere is your hint!:{hint}")

        except ValueError or AttributeError:
            print("You have chosen to not view a hint for this question. Good Luck!")

