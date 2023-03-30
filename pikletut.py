import pickle
# cars =  ["Audi","BMW","Suzuki","Rangerover"]
# file = "mycars.pickle"
# fileobj = open(file,"wb")
# pickle.dump(cars,fileobj)
# fileobj.close()

file = "mycars.pickle"
fileobj = open(file,"rb")
mycar = pickle.load(fileobj)
print(mycar)
print(type(mycar))