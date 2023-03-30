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
        return cls(*string.split("-"))

    @staticmethod
    def printgod(string):
        print("HAREKRISHNA\n" + string)

class Programmer(Employee):
    no_of_holiday = 55
    def __init__(self,aname,asalary,arole,language):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.language = language

    def printlog(self):
        return f"The programmer name is {self.name},salary is {self.salary} and role is {self.role}"


pradeep = Employee("Pradeep","200000","Project Manager")
sonam = Employee("sonam",200000,"Instructor")
rakshya = Employee.from_str("Rakshya-200000-Banker")

subham = Programmer("subham",555,"programmer",["python"])
karan = Programmer("karan",555,"programmer",["python"])

print(karan.printlog())
print(karan.no_of_holiday)
