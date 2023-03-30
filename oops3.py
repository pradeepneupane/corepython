class Employee:
    no_of_leaves = 8

    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"Name is {self.name},salary is {self.salary} and role is {self.role}"

pradeep = Employee("Pradeep","200000","Project Manager")
# pradeep = Employee()
# sonam = Employee()
#
# pradeep.name = "Pradeep"
# pradeep.salary = 200000
# pradeep.role = "project manager"

# sonam.name = "Sonam"
# sonam.salary = 200000
# sonam.role = "Instructor"
#
# print(pradeep.printdetails())
# print(sonam.printdetails())

print(pradeep.salary)