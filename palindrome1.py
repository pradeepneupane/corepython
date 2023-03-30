print("Enter a number")
num = int(input())
temp = num
reverse = 0

while(num>0):
    dig = num%10
    reverse = reverse * 10 + dig
    num = num//10

if temp == reverse:
    print("Number is palindrome")

else:
    print("Number is not palidrome")
