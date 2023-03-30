"""
take age or year or birth as input from the user and tell them when they will they turn 100 years old.
Don't use any type of module like datetime or datautils.They can them optionally provide a year and your
program must tell their age in that particular age
-you should be handling all sorts of error
-you seems to oldest
-you can also handling any other error if possible!
"""
age = int(input("Enter your age\n"))

if age>1900:
    db = 2023-age
    #process to convert year into age
    print("your age is:\n", db)
else:
    db = age
    print("your age is:\n", db)

y = 100-db
print(f"you will turn 100 years after {y} years")

a = 2090- 2023
#Difference between current year and given year
x = a + db
print("your age after 2090 is:\n", x)

if db == 0:
    print("you are not born")

elif db >= 100:
    print("you seems to be oldest")

elif db <= 100:
    print("you can enjoy your life")

else:
    exit()

