import random
lst = ['s','w','g']

chances = 10
no_of_chances = 0
computer_point = 0
human_point = 0

print("\t \t \t snake,water,gun game\n\n")

print("s for snake\nw for water\ng for gun\n")

#making the game in while
while(no_of_chances<chances):
    _input = input('snake,water,gun:')
    _random = random.choice(lst)

    if _input==_random:
        print("tie both 0 point each\n")

    #if user enter s
    elif _input=="s" and _random=="g":
        computer_point=computer_point+1
        print(f"your guess{_input} and computer guess is{_random}\n")
        print("computer wins 1 point\n")
        print(f"computer point is {computer_point} and your point is {human_point}")

    elif _input=="s" and _random =="w":
        human_point = human_point+1
        print(f"your guess{_input} and computer guess is{_random}\n")
        print("human wins 1 point\n")
        print(f"computer point is {computer_point} and your point is {human_point}")

        # if user enter w
    elif _input == "w" and _random == "s":
        computer_point = computer_point + 1
        print(f"your guess{_input} and computer guess is{_random}\n")
        print("computer wins 1 point\n")
        print(f"computer point is {computer_point} and your point is {human_point}")

    elif _input == "w" and _random == "g":
        human_point = human_point + 1
        print(f"your guess{_input} and computer guess is{_random}\n")
        print("human wins 1 point\n")
        print(f"computer point is {computer_point} and your point is {human_point}")

        # if user enter g
    elif _input == "g" and _random == "w":
        computer_point = computer_point + 1
        print(f"your guess{_input} and computer guess is{_random}\n")
        print("computer wins 1 point\n")
        print(f"computer point is {computer_point} and your point is {human_point}")

    elif _input == "g" and _random == "s":
        human_point = human_point + 1
        print(f"your guess{_input} and computer guess is{_random}\n")
        print("human wins 1 point\n")
        print(f"computer point is {computer_point} and your point is {human_point}")

    else:
        print("you enter wrong input\n")

    no_of_chances = no_of_chances+1
    print(f"{chances-no_of_chances} is left out of {chances}\n")

print("Game over\n")

if computer_point==human_point:
    print("tie")

elif computer_point>human_point:
    print("computer wins and you loose")

else:
    print("you win and computer loose")

print(f"your point is {human_point} and computer point is {computer_point}")

#
# snake water fun game in python
#the snake drinks the water, the gun shoots the snake and gun has no effect on water

