"""
Python problem 5(Easy, 10 points) palindromeify the list
you are given a list which contains some numbers. you have to print a list of next palindromes only if the number
is greater than 10 otherwise you will print that number
Input = [1, 6, 87, 43]
output = [1, 6, 88, 44]
"""
def next_palindrome(n):
    n = n+1
    while not is_palindrome(n):
        n+= 1
        return n

def is_palindrome(n):
    return str(n) == str(n)[::-1]

if __name__ == '__main__':
    size = int(input("Enter the size of the number"))
    num_list = []
    for i in range(size):
        num_list.append(int(input("Enter the number")))

    print(num_list)

    new_list = []
    for element in new_list:
        if element>10:
            n = next_palindrome(element)
            new_list.append(n)
        else:
            new_list.append(n)

    # print(f"Output List: {[num_list[i] if num_list[i] < 10 else next_palindrome(num_list[i]) for i in range(size)]}")


