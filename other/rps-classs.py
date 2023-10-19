import random

class Rock_paper_scissors:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.player_score = 0
        self.computer_score = 0
        self.rounds_played = 0

    def play_game(self):
        while True:
            player_choice = input("\033[34mChoose rock, paper or scissors: \033[0m")
            computer_choice = random.choice(self.choices)

            print(f"\033[33mPlayer choice: {player_choice}\033[0m")
            print(f"\033[33mComputer choice: {computer_choice}\033[0m")

            if player_choice not in self.choices:
                print("\033[33mInvalid choice. Try again.\033[0m")
            elif player_choice == computer_choice:
                print("\033[31mIt's a tie!\033[0m")
            elif (player_choice == 'rock' and computer_choice == 'scissors'):
                print("\033[31mYou win!\033[0m")
                self.player_score += 1
            elif (player_choice == 'paper' and computer_choice == 'rock'):
                print("\033[31mYou win!\033[0m")
                self.player_score += 1
            elif (player_choice == 'scissors' and computer_choice == 'paper'):
                print("\033[31mYou win!\033[0m")
                self.player_score += 1
            else:
                print("\033[31mThe computer wins!\033[0m")
                self.computer_score += 1

            self.rounds_played += 1

            print(f"\033[34mRounds played: {self.rounds_played}\033[0m")
            print(f"\033[34mPlayer score: {self.player_score}\033[0m")
            print(f"\033[34mComputer score: {self.computer_score}\033[0m\n")

            play_again = input("\033[31;5mDo you want to play again? (y/n) \033[0m")
            if play_again.lower() == 'y':
                continue
            else:                
                print("\033[33mThanks for playing!\033[0m")
                break

play = Rock_paper_scissors()
play.play_game()