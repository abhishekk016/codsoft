import tkinter as tk
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors Game")
        self.user_score = 0
        self.computer_score = 0

        # Display the welcome message
        self.welcome_label = tk.Label(root, text="Welcome to Rock, Paper, Scissors!", font=("Arial", 16))
        self.welcome_label.pack(pady=10)

        self.instructions_label = tk.Label(
            root, 
            text="Click one of the buttons below to make your choice.\nRock beats Scissors, Scissors beats Paper, Paper beats Rock.", 
            font=("Arial", 12),
            justify="center"
        )
        self.instructions_label.pack(pady=10)

        # Buttons for Rock, Paper, Scissors
        self.rock_button = tk.Button(root, text="Rock", width=20, height=2, font=("Arial", 14), command=self.play_rock)
        self.rock_button.pack(pady=10)

        self.paper_button = tk.Button(root, text="Paper", width=20, height=2, font=("Arial", 14), command=self.play_paper)
        self.paper_button.pack(pady=10)

        self.scissors_button = tk.Button(root, text="Scissors", width=20, height=2, font=("Arial", 14), command=self.play_scissors)
        self.scissors_button.pack(pady=10)

        # Label to show the game result
        self.result_label = tk.Label(root, text="Make your choice!", font=("Arial", 14))
        self.result_label.pack(pady=20)

        # Label to show the score
        self.score_label = tk.Label(root, text="Score -> You: 0, Computer: 0", font=("Arial", 14))
        self.score_label.pack(pady=10)

        # Button to restart the game
        self.restart_button = tk.Button(root, text="Restart", width=20, height=2, font=("Arial", 14), command=self.restart_game)
        self.restart_button.pack(pady=20)

    def get_computer_choice(self):
        """Function to get the computer's choice."""
        choices = ["rock", "paper", "scissors"]
        return random.choice(choices)

    def determine_winner(self, user_choice, computer_choice):
        """Function to determine the winner of the game."""
        if user_choice == computer_choice:
            return "It's a tie!", 0, 0
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            return "You win!", 1, 0
        else:
            return "Computer wins!", 0, 1

    def update_score(self):
        """Update the score label."""
        self.score_label.config(text=f"Score -> You: {self.user_score}, Computer: {self.computer_score}")

    def play_rock(self):
        self.play_game("rock")

    def play_paper(self):
        self.play_game("paper")

    def play_scissors(self):
        self.play_game("scissors")

    def play_game(self, user_choice):
        """Function to play the game."""
        computer_choice = self.get_computer_choice()

        result, user_win, computer_win = self.determine_winner(user_choice, computer_choice)

        self.user_score += user_win
        self.computer_score += computer_win

        # Show the result of the round
        self.result_label.config(
            text=f"You chose {user_choice.capitalize()}.\nThe computer chose {computer_choice.capitalize()}.\n{result}"
        )

        # Update the score display
        self.update_score()

    def restart_game(self):
        """Restart the game by resetting the scores and labels."""
        self.user_score = 0
        self.computer_score = 0
        self.result_label.config(text="Make your choice!")
        self.update_score()

# Create the main window
root = tk.Tk()
game = RockPaperScissorsGame(root)
root.mainloop()
