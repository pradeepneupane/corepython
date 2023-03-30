print("Enter a first number")
num1 = int(input())

print("Enter second number")
num2 = int(input())

print("Enter a choice"+'+-*/')
num3 = input()

if num1==45 and num2==3 and num3=='*':
    print("555")

elif num1==56 and num2==9 and num3=='+':
    print("77")

elif num1==56 and num2==9 and num3=='/':
    print("9")

elif num3 =='+':
    plus = num1+num2
    print("plus")

elif num3 =='-':
    sub = num1-num2
    print(sub)

elif num3 =='*':
    mul = num1*num2
    print(mul)

elif num3 =='/':
    div = num1/num2
    print(div)

else:
    print("Error!please check your input")
# if 45*3:
#     print(555)
# elif 56+9:
#     print(77)
# elif 56/9:
#     print(9)
