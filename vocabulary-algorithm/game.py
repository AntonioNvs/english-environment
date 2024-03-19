import os
import time
import random
import pandas as pd

class Game:
    def __init__(self) -> None:
        self.words_data = pd.read_csv("data/words.csv")

    def print_initial_screen(self):
        print("Welcome to the vocabulary game!")
        print("For each word, you need to define if the word exists or not")
        print("Type 'y' for yes and 'n' for no")
        print("You can type 'exit' to exit the game.\n")

    def start_game(self):
        self.print_initial_screen()

        while True:
            word, exists = self.round_word()

            print(f"The word is: {word}")

            user_input = input("R: ")

            if user_input == "exit":
                break
            if (user_input == "y" and exists) or (user_input == "n" and not exists):
                print("Correct!")
            else:
                print("Incorrect!")

            time.sleep(2)
            os.system("cls")

    def round_word(self):
        word = self.selected_random_word()

        if random.random() >= 0.5:
            return word, True
        else:
            return self.modify_word(word), False

    def modify_word(self, word):
        word = list(word)
        random_index = random.randint(0, len(word) - 1)
        word[random_index] = random.choice("abcdefghijklmnopqrstuvwxyz")

        return "".join(word)
    
    def selected_random_word(self):
        return self.words_data.sample().iloc[0]['word']
        


if __name__ == "__main__":
    Game().start_game()