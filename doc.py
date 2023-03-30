# def function1():
#     print("subscribe now")
#
# func2 = function1
# del function1
# func2()

# def funcreturn(num):
#     if num==0:
#         return print
#     if num==1:
#         return sum
#
# a = funcreturn(1)
# print(a)

# def executor(func):
#     func("this")
#
# executor(print)

def dec1(func1):
    def nowexec():
        print("Executing now")
        func1()
        print("Executed")
    return nowexec

@dec1
def w():
    print("Pradeep is a krishna's friend")

w()
