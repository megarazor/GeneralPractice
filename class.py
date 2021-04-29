class Base:
    def __init__(self):
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks"
    def print(self):
        print(self.__c)
    def return__c(self):
        return self.__c
 
# Creating a derived class
class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Devired:", Base.return__c(self))
    def print_(self):
        Base.print(self)
# Driver code
obj1 = Base()
obj2 = Derived()
# print(obj1.a)
obj1.print()

# obj2 = Derived()
