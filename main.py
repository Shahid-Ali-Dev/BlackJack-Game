from art import logo
import random
print(logo)
def again():
    """Use it to restart the game"""
    ask = input("Do you want to play the game? Type 'y' for yes and 'n' for no\n").lower()
    if ask == "y":
        bj = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        you = []
        computer = []
        def shuffle_you():
            """Adds a random card to our deck"""
            random.shuffle(bj)
            you.append(bj[0])
            if bj[0] == 11 and sum(you) > 21:
                you.remove(11)
                you.append(1)

        def shuffle_computer():
            """Adds a random card to computer's deck"""
            random.shuffle(bj)
            computer.append(bj[0])
            if bj[0] == 11 and sum(computer) > 21:
                computer.remove(11)
                computer.append(1)

        def shuffle1():
            """Use it to add a random card to our deck and also print the score of player"""
            shuffle_you()
            print(f"    Your current cards: {you}, and Your total score: {sum(you)}")

        def printing():
            """Prints the final score of both parties."""
            print(f"    Your final cards: {you}, and Your final score: {sum(you)}")
            print(f"    Computer final cards: {computer}, and Computer final score: {sum(computer)}")

        shuffle_you()
        shuffle1()
        shuffle_computer()
        score = True
        if sum(you) == 21:
            print(f"    Computer first card: {computer[0]}, and Computer total score: {computer[0]}")
            print("OHH Wow, it seems like your luck is in favour because you've hit the blackjack.\nYou won!!!")
            again()
        else:
            while score:
                print(f"    Computer first card: {computer[0]}, and Computer total score: {computer[0]}")
                hit = input("Type 'h' to hit another card or 's' to stand:\n ").lower()
                if hit == "h":
                    shuffle1()
                    if sum(computer) <= 18:
                        shuffle_computer()

                    if sum(you) == sum(computer) and sum(computer) == 21:
                        printing()
                        print("Its a draw")
                        score = False

                    elif sum(you) == 21:
                        score = False
                        printing()
                        print("Congrats you won, its a winner winner chicken dinner.")

                    elif sum(you) > 21 and  sum(computer) > 21:
                        printing()
                        print("Both the player and the computer lost.")
                        score = False
                    elif sum(you) > 21 or sum(computer) == 21:
                        printing()
                        print("Sorry pal, it seems like your luck ran out\nYou Lose, Game Over.")
                        score = False
                else:
                    print(f"    Your current cards: {you}, and Your total score: {sum(you)}")
                    while sum(computer) < 19:
                        shuffle_computer()
                    if sum(you) == sum(computer):
                        printing()
                        print("Its a draw")
                        score = False

                    elif sum(computer) > 21 and sum(you) > 21:
                        printing()
                        print("Both the player and the computer lost.")
                        score = False

                    elif sum(you) > 21 or sum(computer) == 21:
                        printing()
                        print("Sorry pal, it seems like your luck ran out\nYou Lose, Game Over.")
                        score = False

                    elif sum(computer) > 21 or sum(you) == 21:
                        printing()
                        print("Computer lost this time, you Won!")
                        score = False

            if not score:
                    again()
again()




