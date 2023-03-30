class Employee:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "Email is not set please it using setter"
        return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter
    def email(self,string):
        print("setting now")
        names = string.split("@")[0]
        self.fname = string.split(".")[0]
        self.lname = string.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

skillf = Employee("Skill","F")
# print(type(skillf))
# print(id("This a string of HAREKRISHNA GOD"))
# print(dir(skillf))

import inspect
print(inspect.getmembers(skillf))