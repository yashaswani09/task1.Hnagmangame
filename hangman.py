import random

class Hangman:
    def __init__(self):
        self.words = ['drums', 'eagle', 'cloud', 'zebra', 'flame']
        self.secret = random.choice(self.words)
        self.display = ['*' for _ in self.secret]
        self.attempts = 6
        self.used = set()

    def play(self):
        print(">> HANGMAN GAME START <<")
        while self.attempts > 0 and '*' in self.display:
            print("Word:", ''.join(self.display))
            print("Used:", ', '.join(sorted(self.used)))
            guess = input("Enter a letter: ").lower()

            if not guess.isalpha() or len(guess) != 1:
                print("Invalid input.")
                continue

            if guess in self.used:
                print("Already tried.")
                continue

            self.used.add(guess)

            if guess in self.secret:
                self.update_display(guess)
                print("Nice one!")
            else:
                self.attempts -= 1
                print("Wrong! Left:", self.attempts)

        self.end_game()

    def update_display(self, char):
        indices = [i for i in range(len(self.secret)) if self.secret[i] == char]
        for i in indices:
            self.display[i] = char

    def end_game(self):
        if '*' not in self.display:
            print("You win! Word was:", self.secret)
        else:
            print("You lost! Word was:", self.secret)

game = Hangman()
game.play()