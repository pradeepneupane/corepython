class Employee:
    no_of_leaves = 8

    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"Name is {self.name},salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves = newleaves

    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary + other.salary

    def __str__(self):
        return f"The name is {self.name},salary is{self.salary} and role is{self.role}"

emp1 = Employee("Pradeep", 500, "Programmer")
# emp2 = Employee("Navraj", 500, "Programmer")

print(emp1)