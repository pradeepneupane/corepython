# #global and local variable
#
# p = 10 #Global
#
# def function1(n):
#     # p = 5 #local
#     global p
#     p = p + 50
#     m = 8 #local
#     print(p, m)
#     print(n, "I have printed")
#
# function1("This is me")
# print(p)
x= 89
def pradeep():
    x = 20
    def harekrishna():
        global x
        x = 88
    harekrishna()
    print("after calling harekrishna()", x)
pradeep()
print(x)