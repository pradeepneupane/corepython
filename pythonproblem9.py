'''
Python practice problem(medium ,10 points)
Its a result day at school and not everyone is happy. You decided to make your friend laugh by
jumbling their names to come up with some funny names
Your program should take the number of names separated by space as a input.Output should be funny
names in one same order
Input:
Enter a number of friends
3
Enter a name of your 3 friends
Pradeep neupane
prabhat kc
prakriti pokherel
output:
pradeep neupane
prabhat pokherel
prakriti kc
'''
import random
def jumble_names():
    # If maxsplit is specified, the list will have the maximum of maxsplit+1 items.
    # Thus in case of lname, even if someone has specified middle name it'll be
    # considered as a whole
    fname = [name.split()[0] for name in names]
    lname = [name.split(" ", 1)[1] for name in names]

    for _ in names:
        random_fname = random.choice(fname)
        random_lname = random.choice(lname)

        print(f"{random_fname} {random_lname}")

        fname.remove(random_fname)
        lname.remove(random_lname)

if __name__ == '__main__':
    print("\t \t \t RESULT DAY \t \t \t")
    number = int(input("Enter the number of friend \n"))
    print(f"Enter the name of your {number} friends \n")

    names = []
    for i in range(number):
        names.append(input("Enter full name \n"))

    jumble_names()
