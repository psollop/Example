#Guess the number: Develop a game where the computer chooses a random number, and
#the player must guess it within a limited number of attempts

import random


def main():
    min_num=1
    max_num=100
    max_attemps=3

    secret_number= random.randint(min_num,max_num)

    print("Welcome to the guess number game")
    print(f"I'm thinking in a number between {min_num} and {max_num}")

    for i in range(1, max_attemps + 1):
        question= int(input (f"You have {i}/{max_attemps} attemps to guess the numer. Enter your number: "))
        if question < secret_number:
            print("Try a higher number")
        elif question>secret_number:
            print("Try a lower number")
        else:
            print(f"You guess the secret number: {secret_number} in {i} attemps")
            break
    else:
        print(f"You loose your attemps, the secret number was {secret_number}")

if __name__ == "__main__" :
    main()

