import random


class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    @classmethod
    def sort(cls, name):
        print(f"{name} is in {random.choice(cls.houses)}")

Hat.sort("Harry")

#Instance Methods vs Class Methods -
#Instance methods are methods that are associated with an instance of a class. They can access and 
# modify the attributes of that instance. 
# They are defined with the "self" parameter, 
# which refers to the instance of the class that is calling the method.

#Instance Variables - a variable that is associated with a specific instance of a class. 
#Denoted by .n where n is the name of the variable. Each instance of a class can have its own unique values for these variables, allowing us to create multiple objects with different attributes.



#Class methods, on the other hand, are methods that are associated with the 
# class itself rather than any particular instance.
# They are defined with the @classmethod decorator and take the class as their first parameter, which is conventionally named "cls". 
# Class methods can access and modify class-level attributes, which are shared among all instances of the class, but they cannot access instance-level attributes directly.

#Class Variables - a variable that is shared among all instances of a class. 
# They are defined within the class but outside of any instance methods.
