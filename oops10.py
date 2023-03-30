class Employee:
    no_of_leaves = 8
    _protect = 3
    __private = 10

    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"Name is {self.name},salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_str(cls,string):
        return cls(*string.split("-"))

    @staticmethod
    def printgod(string):
        print("HAREKRISHNA\n" + string)

emp = Employee("Pradeep", 700, "Programmer")

print(emp._Employee__private)
# print(emp._protect)