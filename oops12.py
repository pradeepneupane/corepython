class A:
    classvar1 = "I am a class var in class A"
    def __init__(self):
        self.var1 = "Iam inside class A constructor"
        self.classvar1 = "Instance variable in class A"
        self.special = "special"

class B(A):
    classvar1 = "I am in class B"

    def __init__(self):
        self.var1 = "Iam inside class A constructor"
        self.classvar1 = "Instance variable in class A"
        super().__init__()

a = A()
b = B()
print(b.var1,b.special)
