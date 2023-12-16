##Dice simulator: Write a program that simulates the roll of two dice and calculates the sum of
##the values obtained.

import random


def roll_two_dice():
    die1 = random.randint(1, 6)  # Roll the first die
    die2 = random.randint(1, 6)  # Roll the second die
    return die1, die2

def main():
    die1, die2 = roll_two_dice()
    print(f"Result of the first die: {die1}")
    print(f"Result of the second die: {die2}")
    print(f"Sum total: {die1 + die2}")

if __name__ == "__main__":
    main()
