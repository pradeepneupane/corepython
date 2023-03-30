""""
python practice problem 4
problem content:
A palindrome is a string which when reverse is equal to itself. Example of palindrome includes 616
mom, 676, 10001
you have to take a number as a input from the user. You have to find next palindrome corresponding
to that number. Your first input showed as number of test cases and the cases as input from
the user
3
451
10
2133
"""
def next_palindrome(n):
    n = n+1
    while not is_palindrome(n):
        n+= 1
        return n

def is_palindrome(n):
    return str(n) == str(n)[::-1]

if __name__ == '__main__':
    n = int(input("Enter a number of test cases/n"))
    numbers = []
    for i in range(n):
        number = int(input("Enter the number\n"))
        numbers.append(number)
        print(numbers)

    for i in range(n):
        print(f"Next palindrome for {numbers[i]} is {next_palindrome(numbers[i])}")
