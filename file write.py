# f = open("pradeep2.txt", "w")
# f.write("Harekrishna is my best friend")
# f.close()
#append
# f = open("pradeep2.txt", "a")
# a = f.write("Krishna is my best friend\n")
# print(a)
# f.close()
#handle read and write both
f = open("pradeep2.txt", "r+")
print(f.read())
f.write("Thank You")