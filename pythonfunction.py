# def myFunction():
#     print("Harekrishna")
#
# myFunction()

# def myFunction(fname):
#     print(fname+" "+"neupane")
#
# myFunction("pradeep")
# myFunction("prabhat")
# myFunction("prakriti")

# def myFunction(fname,lname):
#     print(fname+" "+lname)
#
# myFunction("Praadeep","Neupane")

# def myFunction(*kids):
#     print("The youngest child is", kids[3])
#
# myFunction("Bindu","Lila","Aarati","Pradeep")

# def myFunction(child4,child3,child2,child1):
#     print("The youngest child is" + child4)
# myFunction(child1="Bindu",child2="Lila",child3="Aarati",child4="Pradeep")

# def myFunction(**kid):
#     print("His last name is" + kid["lname"])
# myFunction(fname = "Pradeep",lname="Neupane")

# def myFunction(country = "Norway"):
#     print("I am from" +country)
#
# myFunction("Nepal")
# myFunction("Usa")
# myFunction()
# myFunction("Austrila")

# def myFunction(food):
#     for i in fruits:
#         print(i)
#
# fruits = ["apple","banana","cherry"]
#
# myFunction(fruits)

# def myFunction(x):
#     return 5 * x
#
# print(myFunction(3))
# print(myFunction(5))
# print(myFunction(10))

# def myFunction():
#     pass

# def tri_recursion(k):
#     if(k>0):
#         result = k + tri_recursion(k-1)
#         print(result)
#     else:
#         result = 0
#     return result
#
# print("\n \n Recursion Result")
# tri_recursion(6)

# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result
#
# print("\n\nRecursion Example Results")
# tri_recursion(6)
def add(a,b):
    return a + b

if __name__ == '__main__':
    a = int(input("Enter your first number \n"))
    b = int(input("Enter second number \n"))
    print("Add two number")
    print(add(a,b))


