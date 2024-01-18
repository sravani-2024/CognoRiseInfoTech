import random

class HangmanGame:
    def __init__(self, word_list):
        self.word_list = word_list
        self.current_word = ""
        self.guesses = []
        self.max_attempts = 6
        self.attempts_left = self.max_attempts

    def select_random_word(self):
        self.current_word = random.choice(self.word_list).upper()

    def initial_display(self):
        return "_ " * len(self.current_word)

    def user_input(self):
        return input("Enter a letter: ").upper()

    def check_letter(self, letter):
        return letter in self.current_word

    def update_state(self, letter):
        self.guesses.append(letter)
        return ' '.join([char if char in self.guesses else '_' for char in self.current_word])

    def hangman_display(self):
        return f"Attempts left: {self.attempts_left}"

    def win_loss_check(self):
        if set(self.current_word) == set(self.guesses):
            return "You win!"
        elif self.attempts_left == 0:
            return f"You lose! The word was {self.current_word}."
        else:
            return None

    def play_again(self):
        return input("Do you want to play again? (yes/no): ").lower() == "yes"


def main():
    word_list = ["PYTHON", "JAVA", "C++", "HTML", "CSS"]
    hangman_game = HangmanGame(word_list)

    while True:
        hangman_game.select_random_word()
        print("Welcome to Hangman!")
        print(hangman_game.initial_display())

        while True:
            guess = hangman_game.user_input()

            if guess.isalpha() and len(guess) == 1:
                if hangman_game.check_letter(guess):
                    print(hangman_game.update_state(guess))
                else:
                    hangman_game.attempts_left -= 1
                    print(hangman_game.hangman_display())

                result = hangman_game.win_loss_check()
                if result:
                    print(result)
                    break
            else:
                print("Please enter a valid single letter.")

        if not hangman_game.play_again():
            break

if __name__ == "__main__":
    main()
