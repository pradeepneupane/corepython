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

class Player:
    no_of_games = 4
    def __init__(self,name,game):
        self.name = name
        self.game = game

    def printdetails(self):
        return f"The name is {self.name},Game is {self.game}"

class Coolprogrammer(Employee,Player):
    language = "Python"
    no_of_games = 9

    def printlanguage(self):
        print(self.language)

pradeep = Employee("Pradeep","200000","Project Manager")
sonam = Employee("sonam",200000,"Instructor")

messi = Player("messi","FootBall")
nabraj = Coolprogrammer("nabraj",850,["python"])

det = messi.printdetails()
print(det)
nabraj.printlanguage()

