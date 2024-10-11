class Student:
    def __init__(self):
        self.__id = 123#Private attribute

Sonam = Student()
print(Sonam._id)   #Attribute error      