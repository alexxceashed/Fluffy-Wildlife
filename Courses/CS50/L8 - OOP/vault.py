class Vault:
    def __init__(self, galleons=0, sickels=0, knuts=0):
        self.galleons = galleons
        self.sickels = sickels
        self.knuts = knuts 

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickels} Sickels, {self.knuts} Knuts"

    def __add__(self,other):  #self is the first operand, other is the second operand
        galleons = self.galleons + other.galleons
        sickels = self.sickels + other.sickels #these are local variables
        knuts = self.knuts + other.knuts
        return Vault(galleons,sickels,knuts)
    ...
potter = Vault(100,50,25)
print(potter)

weasley = Vault(25,50,100)
print(weasley)  

#Operator Overloading
total = potter + weasley 
print(f"Merged Vault: {total}")