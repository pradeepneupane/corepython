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

pradeep = Employee("Pradeep","200000","Project Manager")
sonam = Employee("sonam",200000,"Instructor")

sonam.change_leaves(34)
print(sonam.no_of_leaves)
