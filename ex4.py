#pattern printing
#input = Interger n
#boolean = True or false
#true n= 5
# *
# **
# ***
# ****
#*****

# i = 1
# j = 1
# while i<=5:
#     while j<=i:
#         print('*', end='')
#         j = j + 1
#         print()
#     i = i+1

n = int(input('Enter number of rows : '))

i = 1
while i <= n:
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()
    i += 1

