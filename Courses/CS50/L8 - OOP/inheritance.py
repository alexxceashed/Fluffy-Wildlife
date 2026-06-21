#Inheritance in Python is a way to create a new class that is a modified version of an existing class. 
# The new class is called a child class, and the existing class is called a parent class. 
# The child class inherits all the attributes and methods of the parent class, and can also have its own attributes and methods.    

class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name
    ...

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name) #Accesses the superclass and assigns the name.
        self.house = house
    ...
class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    ...

wizard = Wizard("Albus")
student = Student("Harry", "Griffindor")

prof = Professor("Severus", "Defence Against The Dark Arts")



#Operator Overloading - for example, the + operator is used for addition but also for string concatenation. 
# In Python, we can define how operators work with our own classes by implementing special methods.