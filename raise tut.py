# a = input("what is your name")
# b = input("How much do you earn")
# if int(b)==0:
#     raise ZeroDivisionError("b is stopping the program")
#
# if a.isnumeric():
#     raise Exception("Numbers arenot allowed")
#
# print(f"hello krishns and his friend {a}")
c = input("Enter your name")
try:
    print(a)
except Exception as e:
    if c=="pradeep":
        raise ValueError("pradeep is blocked")
    print("Exception handled")