class Dad:
    basketball = 6

class Son(Dad):
    dance = 1
    basketball = 9

    def isdance(self):
        return f"yes i dance{self.dance} no of times"

class Grandson(Son):
    dance = 6
    guitar  = 1

    def isdance(self):
        return f"jackson yeah!"
        return f"yes i dance very awesome{self.dance} no of times"

keshav = Dad()
Rukmagat = Son()
Pradeep = Grandson()

print(Pradeep.basketball)
print(Pradeep.guitar)