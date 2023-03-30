# i = 0
# while(True):
#     print(i+1, end=" ")
#     if(i==44):
#         break
#     i = i+1
# i = 0
# while(True):
#     if i+1<5:
#         i = i+1
#         continue
#     print(i+1, end=" ")
#     if(i==45):
#         break
#     i = i+1
# i = int(input())
# while(True):
#     if i+1<100:
#         i=i+1
#         continue
#     print(i+1)
#     if(i==99):
#         break
#     i = i+1
while(True):
    inp = int(input("Enter a number\n"))
    if inp>100:
        print("Congratulaton you have enter greater than 100")
        break
    else:
        print("Try Again")
        continue
