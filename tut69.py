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

nepali_supporter = Employee("Nepali","supporter")
print(nepali_supporter.email)
nepali_supporter.fname = "US"
print(nepali_supporter.email)

nepali_supporter.email = "this.that@gmail.com"
print(nepali_supporter.fname)

del nepali_supporter.email
print(nepali_supporter.email)

