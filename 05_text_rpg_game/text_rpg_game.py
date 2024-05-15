from random import random, randint, choice

import threading

import time

from math import floor


class TextRPG:
    def __init__(self):
        self.player = self.initialize_game()
        self.run_game()

    def initialize_game(self):
        print("-" * 100)
        print("Welcome to text RPG game")
        print(
            "Note: Player HP will decrease by 1 in every second. So, use medkit to survive!"
        )
        print("-" * 100)
        name = input("Enter your character's name: ")
        player = self.Player(name, 5, 100)
        return player

    def reduce_health(self):
        while True:
            self.main_character().reduce_health = 1
            if self.main_character()._health == 0:
                print("")
                print("-" * 100)
                print(f"Your HP was {self.main_character()._health}! Game Over🥲")
                print("Thanks for playing!")
                print("-" * 100)
                quit()
            time.sleep(1)

    def run_game(self):
        self.display_palyer_info()

    def main_character(self):
        return self.player

    def display_palyer_info(self):
        print("-" * 100)
        print("Player Information!")
        print(f"Name: {self.player._name}")
        print("Health: 100")
        print("-" * 100)
        threading.Thread(target=self.reduce_health).start()
        self.main_menu()

    def solve_math_problem(self):
        random_time = randint(5, 10)
        operations_list = ["+", "-", "*", "/", "**"]
        operation = choice(operations_list)

        if operation == "+":
            a = floor(random() * 100)
            b = floor(random() * 100)
            start_time = time.time()
            user_result = input(
                f"What's {a} + {b}? You have {random_time} s to answer this."
            )
            end_time = time.time()
            elapsed_time = end_time - start_time
            print("-" * 100)
            result = a + b
            if elapsed_time > random_time:
                print("Times Up! You did not answered in time.")
            elif user_result == str(result):
                print("-" * 100)
                self.main_character().increase_med_count = 1
                print(
                    f"You answered in {floor(elapsed_time)}s so You earned a med kit! You have now in total {self.main_character()._revival_med_count} MED"
                )

                print("-" * 100)

            else:
                print("-" * 100)
                print(f"Sorry, but your answer was wrong! The right answer is {result}")
                print("-" * 100)
        elif operation == "-":
            a = floor(random() * 100)
            b = floor(random() * 100)
            start_time = time.time()
            user_result = input(
                f"What's {a} - {b}? You have {random_time} s to answer this."
            )
            end_time = time.time()
            elapsed_time = end_time - start_time
            print("-" * 100)
            result = a - b
            if elapsed_time > random_time:
                print("Times Up! You did not answered in time.")
            elif user_result == str(result):
                print("-" * 100)
                self.main_character().increase_med_count = 1
                print(
                    f"You answered in {floor(elapsed_time)}s so You earned a med kit! You have now in total {self.main_character()._revival_med_count} MED"
                )

                print("-" * 100)

            else:
                print("-" * 100)
                print(f"Sorry, but your answer was wrong! The right answer is {result}")
                print("-" * 100)

        elif operation == "*":
            a = randint(0, 20)
            b = randint(0, 10)
            start_time = time.time()
            user_result = input(
                f"What's {a} * {b}? You have {random_time} s to answer this."
            )
            end_time = time.time()
            elapsed_time = end_time - start_time
            print("-" * 100)
            result = a * b
            if elapsed_time > random_time:
                print("Times Up! You did not answered in time.")
            elif user_result == str(result):
                print("-" * 100)
                self.main_character().increase_med_count = 1
                print(
                    f"You answered in {floor(elapsed_time)}s so You earned a med kit! You have now in total {self.main_character()._revival_med_count} MED"
                )

                print("-" * 100)

            else:
                print("-" * 100)
                print(f"Sorry, but your answer was wrong! The right answer is {result}")
                print("-" * 100)
        elif operation == "/":
            a = randint(0, 20)
            b = randint(1, 10)
            start_time = time.time()
            user_result = input(
                f"What's {a} / {b}? Enter only the integer value. You have {random_time} s to answer this."
            )
            end_time = time.time()
            elapsed_time = end_time - start_time
            print("-" * 100)
            result = floor(a / b)
            if elapsed_time > random_time:
                print("Times Up! You did not answered in time.")
            elif user_result == str(result):
                print("-" * 100)
                self.main_character().increase_med_count = 1
                print(
                    f"You answered in {floor(elapsed_time)}s so You earned a med kit! You have now in total {self.main_character()._revival_med_count} MED"
                )
                print("-" * 100)

            else:
                print("-" * 100)
                print(
                    f"Sorry, but your answer was wrong! The right integer answer is {result}"
                )
                print("-" * 100)
        elif operation == "**":
            a = randint(0, 5)
            b = randint(1, 4)
            start_time = time.time()
            user_result = input(
                f"What's {a} power {b}? You have {random_time} s to answer this."
            )
            end_time = time.time()
            elapsed_time = end_time - start_time
            print("-" * 100)
            result = a**b
            if elapsed_time > random_time:
                print("Times Up! You did not answered in time.")
            elif user_result == str(result):
                print("-" * 100)
                self.main_character().increase_med_count = 1
                print(
                    f"You answered in {floor(elapsed_time)}s so You earned a med kit! You have now in total {self.main_character()._revival_med_count} MED"
                )

                print("-" * 100)

            else:
                print("-" * 100)
                print(f"Sorry, but your answer was wrong! The right answer is {result}")
                print("-" * 100)

    def earn_medkit(self):
        while True:
            print("-" * 100)
            print("You have two options to earn medkit.")
            print(
                "1. Solve a math problem which includes Addition, Substraction, Multiplication, or Division in a given amount of time. But you will loose your HP by 5."
            )
            print("2. Wait until random medkit drops.")
            print("3. Don't want to earn medkit.")
            user_input = input("Whats your choice? ")
            print("-" * 100)
            if user_input == "1":
                self.solve_math_problem()
            elif user_input == "2":
                pass
            elif user_input == "3":
                break
            else:
                print("Invalid option chosen! Please try again.")

    def main_menu(self):
        try:
            while True:
                print("-" * 100)
                print("1: View Player Health")
                print("2. View Player Inventory")
                print("3. Increase your health")
                print("4. Collect MED count")
                print("5. Quit Game")
                print("-" * 100)
                choice = input("What do you want to choose? ")

                if choice == "1":
                    self.main_character().player_health()
                    continue

                elif choice == "2":
                    self.main_character().player_inventory()

                elif choice == "3":
                    self.main_character().revive_health = 10
                    continue
                elif choice == "4":
                    self.earn_medkit()

                elif choice == "5":
                    break
                else:
                    print("-" * 100)
                    print("Invalid Option Chosen! Please try again")
                    print("-" * 100)
        except:
            print("-" * 100)
            print("Exiting the game. Thanks for playing!")
            print("-" * 100)
            exit()

    class Player:
        def __init__(self, name, revival_med_count, hp):
            self._name = name
            self._health = hp
            self._revival_med_count = revival_med_count

        def player_health(self):
            print("-" * 100)
            print(f"Player Health: {self._health}")
            print("-" * 100)

        def player_inventory(self):
            print("-" * 100)
            print(
                f"You have {self._revival_med_count} health revival left in your inventory. Health revival will increase your HP by 10"
            )
            print("-" * 100)

        def current_hp(self):
            print("-" * 100)
            print(
                f"Your HP has been increased by 10 with total {self._health} HP and {self._revival_med_count} MED count left."
            )
            print("-" * 100)

        @property
        def reduce_health(self):
            return self._health

        @reduce_health.setter
        def reduce_health(self, value):
            self._health -= value

        @property
        def increase_med_count(self):
            return self._revival_med_count

        @increase_med_count.setter
        def increase_med_count(self, value):
            self._revival_med_count += value
            self._health -= 5

        @property
        def revive_health(self):
            return self._health

        @revive_health.setter
        def revive_health(self, value):

            if self._revival_med_count < 1:
                print("-" * 100)
                print(
                    "Your HP increasing MED count is 0. Please collect more to increase your HP."
                )
                print("-" * 100)
            else:
                if self._health <= 90:
                    self._revival_med_count -= 1
                    self._health += value
                    self.current_hp()
                elif self._health == 100:
                    print("-" * 100)
                    print("You current HP is at Maximum capacity")
                    print("-" * 100)
                else:
                    hp_required = 100 - self._health
                    self._revival_med_count -= 1
                    self._health += hp_required
                    self.current_hp()


def main():
    game = TextRPG()


if __name__ == "__main__":
    main()
