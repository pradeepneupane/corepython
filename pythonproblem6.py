"""""
python problem 6(Easy, 10)
The task you have to perform is "Guess the number". This task consists of 10 point to evaluate your performance
problem statement
Generate a random integer from a to b. You and your friend have to guess a number between a and b. a and b are
input taken from the user. Your friend is player1 and player first. He will have to keep choosing the number,
and your program must tell whether the number is greater than the actual number or less than the actual number
. log the number of trails it took your friend to arrive at that number. You play the same game and then the
person with the minimum numbers of trails wins! Randomly only generates a number after taking a and b as input
and don't show that to the user
Input:
Enter the value of a
4
Enter the value of b
13
output:
player1:
please guess the number between 4 and 13
5
wrong guess! a grater number again
8
wrong guess! a smaller number again
6
correct, you took 3 trails to guess the number
player2:
correct, you took 7 trails to guess the number
player1 wins!
Accepting a coding challenge is an excellent way to improve your coding skills. So keep practicing and keep
yourself up to date.
"""
import random
def guessGame(a,b,actual):
    guess = int(input(f"Guess the number between {a} and {b} \n"))
    nguess = 1
    while guess!=actual:
     if guess < actual:
         guess = int(input("Enter a bigger number/n"))
         nguess += 1
     else:
        guess = int(input("Enter a smaller number/n"))
        nguess += 1

    print(f"you guess the number in {nguess} guess\n")
    return nguess


if __name__ == '__main__':
    a = int(input("Enter the value of a\n"))
    b = int(input("Enter the value of b\n"))
    actual = random.randint(a,b)

    print("player's1 turn\n")
    g1 = guessGame(a,b,actual)

    print("player's 2 turn\n")
    g2 = guessGame(a,b,actual)

    print(g2,g1)

    if g1<g2:
        print("player1 won the game")

    elif g1>g2:
        print("player2 won the match\n")

    else:
        print("Its a tie\n")

    print(f"The number for player1 is {g1} and number for player2 is {g2}")
