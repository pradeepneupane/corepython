import random
def guessGame(a,b,actual):
    guess = int(input(f"Guess the number between {a} and {b} \n"))
    nguess = 1
    while guess!=actual:
        if guess<actual:
            guess = int(input("Enter a bigger number \n"))
            nguess += 1
        else:
            guess = int(input("Enter a smaller number \n"))
            nguess += 1

    print(f"you guess a number in {nguess} guess \n")
    return nguess

if __name__ == '__main__':
    a = int(input("Enter the value of a \n"))
    b = int(input("Enter the value of b \n"))
    actual = random.randint(a,b)

    print("player1's turn \n")
    player1 = guessGame(a,b,actual)

    print("player2's turn \n")
    player2 = guessGame(a,b,actual)

    print("player3's turn \n")
    player3 = guessGame(a,b,actual)

    # newlist = []
    # newlist.append(player1)
    # newlist.append(player2)
    # newlist.append(player3)
    # print(newlist)

    if (player1<player2) and (player1<player3):
        print("player1's win")

    elif (player2<player1) and (player2<player3):
        print("player2's win")

    else:
        print("player3's win")

    print(f"The number for player1's  {player1}, player2's {player2} and player3's {player3}")