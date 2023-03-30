class Employee:
    no_of_leaves = 8

pradeep = Employee()
sonam = Employee()

pradeep.name = "Pradeep"
pradeep.salary = 200000
pradeep.role = "project manager"

sonam.name = "Sonam"
sonam.salary = 200000
sonam.role = "Instructor"

print(pradeep.name,pradeep.salary,pradeep.role)
print(sonam.name,sonam.salary,sonam.role)

print(pradeep.no_of_leaves)
print(sonam.no_of_leaves)
print(sonam. __dict__)
Employee.no_of_leaves = 9
print(Employee. __dict__)
print(Employee.no_of_leaves)

