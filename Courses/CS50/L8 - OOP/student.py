class Student:
    def __init__(self, name, house):  #Initializer method - a special method that is called when an object is created from a class. It is used to initialize the attributes of the object with specific values. In this case, we are using the initializer method to set the name and house attributes of a student object based on user input.
        #properties - attribute that has defense mechanisms put into place to prevent programmers from 
        #calling the instance variables.
    
        self.name = name 
        self.house = house  #self.house runs the setter function. house is the arg, passed over to that function.


        #Instance variable - a variable that is associated with a specific instance of a class. 
        #In this case, we are using instance variables to store the name and house of a student object. 
        # Each student object will have its own unique values for these variables, allowing us to create multiple student 
        # objects with different names and houses.
        
    def __str__(self):  #String representation method - 
        #a special method that is called when an object is converted to a string. 
        # It is used to provide a human-readable representation of the object. 
        # In this case, we are using the string representation method to return a 
        # string that includes the name and house of a student object.
        return f"{self.name} from {self.house}"
    

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)
    
    # @property
    # def name(self):
    #     return self._name 
    
    # @name.setter
    # def name(self, name):
    #     if not name:
    #         raise ValueError("Missing name")
    #     self._name = name #instance variable



    # @property
    # def house(self): #Getter - a method that is used to retrieve the value of an attribute. - @Property
    #     return self._house
    
    # @house.setter
    # def house(self, house): #Setter - a method that is used to set the value of an attribute.  - @house.setter
    #     #In this case, we are using a setter method to set the value of the house attribute of a student object. 
    #     # This allows us to change the house of a student object after it has been created.

    #     houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    #     if house in houses:
    #         self._house = house  #This is the instance variable used for the house.
    #     else:
    #         raise ValueError("Invalid House.")
        

def main():
    student = Student.get()
    # print(f"{student.name} from {student.house}")
    # print("Expecto Patronum!")
    # print(student.charm())
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)  
    #constructor - a special method that is called when an object is created from a class. 
    # It is used to initialize the attributes of the object with specific values. 
    # In this case, we are using the constructor to create a new Student object and set its name and house attributes based on user input.
    
    
    #methods - it is a function that is associated with an object and can be called on that object to perform a specific action or retrieve information. 
    # In this case, we are using the Student class to create a student object and then calling the get_student method to populate the student's name and house attributes based on user input. 
    # The get_student method is responsible for gathering the necessary information from the user and returning a fully initialized student object that can be used 
    # in the main function to display the student's details.
   





#class - A class is a blueprint for creating objects that 
# encapsulate data and behavior. In this case, 
# we could define a Student class with attributes 
# for name and house, 
# and methods to manipulate or retrieve that data. 
# Using a class allows us to create multiple student 
# objects, each with its own unique name and house, 
# while also providing a structure for organizing 
# related functionality.




#Tuple - mainly used to group together related data, 
# and they are immutable, meaning that once you 
# create a tuple, you cannot change its contents. 
# In this case, we are using a tuple to store the 
# name and house of a student together as a single 
# unit of data. This allows us to easily pass around 
# the student's information as one object, rather than 
# having to manage separate variables for the name and house.


#Whereas a list is used in scenarios where you need to store 
# a collection of items that may change over time, 
# such as a list of students in a class. Lists are 
# mutable, meaning you can add, remove, or modify 
# items after the list has been created. In contrast, 
# tuples are used when you want to group together related 
# data that should not be changed, such as the name and 
# house of a student in this example.
if __name__ == "__main__":
    main()
