"""
python problem 8 (Easy, 10 points)
Rohan Das is a fraud
Rohan Das is a fraud by nature. Rohan Das wrote a python function to print a multiplication table of a given number and
put one of the values(Randomly generated) as wrong. Rohan Das did this to fool his classmate and make them commit a mis-
take in a test. You cannot tolerate this
so, you decided to use your python skills to counter Rohan's action by written a python program that validate Rohan's
multiplication table
your function should be able to find out  the wrong value in Rohan's table and expose Rohan Das as a fraud
Note: Rohan's function return a list of a number like this
Rohan Das function input:
rohanMultiplication(6):
Rohan's function returns this output
[6,12,15,26...60]
You have to write a function is correct (table,number) and return the index where Rohan's function is wrong and print
it screen if the table is correct your function returns none.
"""
import random
def rohanMultiplication(number):
    wrong = random.randint(0,9)
    table = [i * number for i in range(1,11)]
    table[wrong] = table[wrong] + random.randint(0,11)
    return table

def isCorrect(table,number):
    for i in range(1,11):
        if table[i-1] != i*number:
            return i-1
    return None

if __name__ == '__main__':
    numbers = int(input("Enter a number:"))
    myTable = rohanMultiplication(numbers)
    print(myTable)
    wrongIndex = isCorrect(myTable,numbers)
    print(f"The table is wrong at {wrongIndex}")

