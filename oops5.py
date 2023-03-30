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

    @classmethod
    def from_str(cls,string):
        # params = string.split("-")
        # return cls(params[0],params[1],params[2])
        return cls(*string.split("-"))

pradeep = Employee("Pradeep","200000","Project Manager")
sonam = Employee("sonam",200000,"Instructor")
rakshya = Employee.from_str("Rakshya-200000-Banker")
#
# sonam.change_leaves(34)
# print(pradeep.no_of_leaves)
print(rakshya.salary)
