# while(True):
#     n = int(input("Enter a number\n"))
#     if n==18:
#         print("congratulation! you're right")
#         break
#     else:
#         print("try again")
#         continue
n=18
number_of_guesses = 1
print("Number of guesses is limited only 9 times")
while(number_of_guesses<=9):
    guess_number = int(input("Guess the number:\n"))
    if guess_number<18:
        print("you enter less number please input greater number\n")
    elif guess_number>18:
        print("you enter greater number please input smaller number\n")
    else:
        print("you won\n")
        print(number_of_guesses, "number of guesses he took to finish\n")
        break
    print(9-number_of_guesses, "number of guesses left")
    number_of_guess = number_of_guesses + 1

if(number_of_guesses>9):
    print("game over")